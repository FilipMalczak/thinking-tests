from thinking_runtime.bootstrap import bootstrap
from thinking_runtime.defaults.logging_config import logging_config, RawHandler
from thinking_runtime.actions import BootstrapActions

from thinking_tests.running.capture_logs import LogCapturer
from thinking_tests.running.test_setup_action import SetupTests

TEST_LOG_CAPTURE_NAME = "Test log capture"

def bootstrap_tests():
    logging_config.handlers.raw.append(RawHandler(TEST_LOG_CAPTURE_NAME, LogCapturer.INSTANCE))

    BootstrapActions.register(SetupTests)

    bootstrap()