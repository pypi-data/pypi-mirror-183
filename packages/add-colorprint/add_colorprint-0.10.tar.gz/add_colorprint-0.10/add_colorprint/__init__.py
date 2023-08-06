from os import name as osname
windowsrechner = osname == "nt"
from winregistry import WinRegistry
from winreg import REG_DWORD


def add_color_print_to_regedit():
    REGEDITPATH = r"HKEY_CURRENT_USER\Console"
    virtualterminalregedit = "VirtualTerminalLevel"
    if windowsrechner:
        try:
            with WinRegistry() as client:
                try:

                    regedit_entry = client.read_entry(
                        REGEDITPATH, virtualterminalregedit
                    )
                    if int(regedit_entry.value) == 1:
                        return True
                    if int(regedit_entry.value) == 0:
                        try:
                            client.write_entry(
                                REGEDITPATH,
                                virtualterminalregedit,
                                value=1,
                                reg_type=REG_DWORD,
                            )
                        except:
                            return False
                except:
                    try:
                        client.write_entry(
                            REGEDITPATH,
                            "VirtualTerminalLevel",
                            value=1,
                            reg_type=REG_DWORD,
                        )

                        return True
                    except:
                        return False
        except:
            pass

