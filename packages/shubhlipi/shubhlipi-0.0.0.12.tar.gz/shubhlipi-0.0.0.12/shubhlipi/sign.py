from .file import cmd
from getpass import getpass
from .kry import tool

def sign_file(loc: str, key=None):
    if key == None:
        key = getpass("sign key = ")
    cmd(
        f'"{tool}//signtool.exe" sign /tr http://timestamp.digicert.com /td sha256 /fd'
        + f' sha256 /f "{tool}//certs//Certificate_key.pfx" /p "{key}" "{loc}"'
    )


def ver_info_add(
    loc: str, ver: str, description="", product="", copyright="", company=""
):
    cmd(
        f'"{tool}//verpatch.exe" "{loc}" {ver}.0.0 /va /pv {ver}.0.0 /s description '
        + f'"{description}" /s product "{product}" /s copyright "{copyright}" /s company "{company}"'
    )


def zipalign_apk(src, dest, file=False):
    print(
        "make",
        cmd(
            f'"{tool}\\android\\zipalign.exe" -p -f -v 4 "{src}" "{dest}"',
            display=False,
            file=file,
        )[0],
    )
    print(
        "verify",
        cmd(
            f'"{tool}\\android\\zipalign.exe" -c -v 4 "{dest}"',
            display=False,
            file=file,
        )[0],
    )


def sign_apk(src, alias, key=None, file=False):
    if key == None:
        key = getpass("sign key = ")
    print(
        "sign",
        cmd(
            f'"{tool}\\android\\apksigner" sign --pass-encoding utf-8 --ks "{tool}\\certs\\certificate.keystore"'
            + f' --ks-key-alias {alias} --ks-pass pass:{key} "{src}"',
            display=False,
            file=file,
        )[0],
    )
    print(
        "verify",
        cmd(
            f'"{tool}\\android\\apksigner" verify "{src}"', display=False, file=file
        )[0],
    )
