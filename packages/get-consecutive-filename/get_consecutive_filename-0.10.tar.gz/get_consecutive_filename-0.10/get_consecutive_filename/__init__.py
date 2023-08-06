import os

import regex


def get_free_filename(folder: str, fileextension: str, leadingzeros: int = 9) -> str:
    if not os.path.exists(folder):
        os.makedirs(folder)
    savefolder_downloads = str(folder).rstrip(r"/\\")
    compiledreg = regex.compile(rf"^0{{0,{leadingzeros-1}}}", regex.IGNORECASE)
    compiledreg_checkfile = regex.compile(
        rf"^\d{{{leadingzeros}}}{fileextension}", regex.IGNORECASE
    )
    newfilenumber = 0
    try:
        picklefiles = os.listdir(f"{savefolder_downloads}{os.sep}")
        picklefiles = [x for x in picklefiles if str(x).endswith(fileextension)]
        picklefiles = [
            x for x in picklefiles if compiledreg_checkfile.search(x) is not None
        ]
        picklefiles = [int(compiledreg.sub("", _.split(".")[0])) for _ in picklefiles]
        newfilenumber = max(picklefiles) + 1
    except Exception as Fehler:
        pass
    finalfile = os.path.normpath(
        path=(
            os.path.join(folder, str(newfilenumber).zfill(leadingzeros) + fileextension)
        )
    )
    return finalfile


