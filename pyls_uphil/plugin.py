import os

from pyls import hookimpl

# If marked with a "tryfirst" or "trylast" option it will be executed first or last respectively in the hook call loop:
# @hookimpl(tryfirst=True)
#
# A hookimpl can be marked with a "hookwrapper" option which indicates that the function will be called to wrap (or surround) all other normal hookimpl calls. A hookwrapper can thus execute some code ahead and after the execution of all corresponding non-wrappper hookimpls.
# @hookimpl(hookwrapper=True)


@hookimpl(hookwrapper=True)
def pyls_document_highlight(config, workspace, document, position):
    outcome = yield
    results = outcome.get_result()

    cwd = "/home/xiaoxiae/Documents/Education/School/MatFyz/Studium/Bakalářské/4. semestr/Ročníkový projekt (RP)/přednáška/uphil/pyls-uphil/pyls_uphil"
    with open(cwd + "/plugin.log", "a") as f:
        f.write(str(("highlight: ", config, workspace, document, position, results)))

    outcome.force_result(results)


@hookimpl(hookwrapper=True)
def pyls_document_symbols(config, workspace, document):
    outcome = yield
    results = outcome.get_result()

    cwd = "/home/xiaoxiae/Documents/Education/School/MatFyz/Studium/Bakalářské/4. semestr/Ročníkový projekt (RP)/přednáška/uphil/pyls-uphil/pyls_uphil"
    with open(cwd + "/plugin.log", "a") as f:
        f.write(str(("highlight: ", config, workspace, document, results)))

    outcome.force_result(results)
