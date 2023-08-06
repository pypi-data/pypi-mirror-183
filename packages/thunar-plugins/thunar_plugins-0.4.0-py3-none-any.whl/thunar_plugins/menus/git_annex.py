# system modules
import logging
import os
import subprocess
import shutil
import shlex

# internal modules
from thunar_plugins import l10n

# external modules
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import GObject, Gtk, Thunarx

logger = logging.getLogger(__name__)


class GitAnnexSubmenu(GObject.GObject, Thunarx.MenuProvider):
    @classmethod
    def name(cls):
        s = _("Git Annex Context-Menu")
        if not shutil.which("git-annex"):
            s = _("[Unavailable]") + " " + s
        return s

    @classmethod
    def description(cls):
        s = _(
            "This plugin adds a context menu item "
            "for managing Git Annex repositories."
        )
        if not shutil.which("git-annex"):
            s += " " + _(
                "Install Git Annex to use this plugin: "
                "https://git-annex.branchable.com"
            )
        return s

    def __init__(self):
        pass

    @classmethod
    def launch_terminal(cls, cmd, cwd):
        cmdparts = [
            "xfce4-terminal",
            "--icon",
            "git-annex",
            "--hide-menubar",
            "--hide-toolbar",
            "--command",
            shlex.join(
                [
                    "sh",
                    "-c",
                    cmd + " && exit "
                    "|| (echo;"
                    "echo 'You can close this window now.';"
                    "sleep infinity)",
                ]
            ),
        ]
        logger.info(f"{cmdparts = }")
        result = subprocess.run(cmdparts, cwd=cwd)

    @classmethod
    def get_git_annex_uuid(cls, folder):
        try:
            return (
                subprocess.check_output(
                    ["git", "-C", folder, "config", "annex.uuid"]
                )
                .decode(errors="ignore")
                .strip()
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Error: {e}")

    def get_file_menu_items(self, window, items):
        folders = set(
            (
                f.get_location().get_path()
                if f.is_directory()
                else os.path.dirname(f.get_location().get_path())
            )
            for f in items
        )
        folder_uuids = {d: self.get_git_annex_uuid(d) for d in folders}
        uuids = set(folder_uuids.values())
        if not (len(uuids) == 1 and all(uuids)):
            logger.debug(
                f"Not exactly ONE unique git-annex repo selected: "
                "{folder_uuids = }"
            )
            return []
        cwd = next(iter(folder_uuids))
        items_quoted = shlex.join(f.get_location().get_path() for f in items)

        git_annex_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnex",
            label=_("Git Annex"),
            tooltip=_("Git Annex"),
            icon="git-annex",
        )

        git_annex_sync_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnex",
            label=_("Sync"),
            tooltip=_("Synchronize Git Annex state with other repos")
            + " (git annex sync)",
            icon="emblem-synchronizing",
        )
        git_annex_sync_menuitem.connect(
            "activate",
            lambda item, cmd: self.launch_terminal(cmd, cwd),
            "(set -x;pwd;git annex sync)",
        )

        git_annex_get_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnex",
            label=_("get"),
            tooltip=_("Retreve files with Git Annex") + " (git annex get)",
            icon="edit-download",
        )
        git_annex_get_menuitem.connect(
            "activate",
            lambda item, cmd: self.launch_terminal(cmd, cwd),
            f"(set -x;pwd;git annex get {items_quoted})",
        )

        git_annex_drop_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnex",
            label=_("drop"),
            tooltip=_("Drop files safely with Git Annex")
            + " (git annex drop)",
            icon="edit-delete",
        )
        git_annex_drop_menuitem.connect(
            "activate",
            lambda item, cmd: self.launch_terminal(cmd, cwd),
            f"(set -x;pwd;git annex drop {items_quoted})",
        )

        git_annex_submenu = Thunarx.Menu()
        git_annex_submenu.append_item(git_annex_sync_menuitem)
        git_annex_submenu.append_item(git_annex_get_menuitem)
        git_annex_submenu.append_item(git_annex_drop_menuitem)
        git_annex_menuitem.set_menu(git_annex_submenu)

        return (git_annex_menuitem,)

    def get_folder_menu_items(self, window, folder):
        return self.get_file_menu_items(window, [folder])
