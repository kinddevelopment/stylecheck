# noinspection PyUnresolvedReferences
from .context import stylecheck
import mock


# noinspection PyUnresolvedReferences
def test_init():
    with mock.patch.object(stylecheck, "main", return_value=42):
        with mock.patch.object(stylecheck, "__name__", "__main__"):
            with mock.patch.object(stylecheck.sys, 'exit') as mock_exit:
                stylecheck.init()
                assert mock_exit.call_args[0][0] == 42
