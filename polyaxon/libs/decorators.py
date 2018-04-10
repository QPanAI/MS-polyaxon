from django.conf import settings


class IgnoreRawDecorator(object):
    """The `IgnoreRawDecorator` is a decorator to ignore raw/fixture data during signals handling.

    usage example:
        @receiver(post_save, sender=settings.AUTH_USER_MODEL)
        @ignore_raw
        def my_signal_handler(sender, instance=None, created=False, **kwargs):
            ...
            return ...
    """

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        if kwargs.get('raw'):
            # Ignore signal handling for fixture loading
            return

        return self.f(*args, **kwargs)


class RunnerSignalDecorator(object):
    """The `RunnerSignalDecorator` is a decorator to ignore signals related to runner.

    This is useful to ignore any signal that is runner specific.

    usage example:
        @receiver(post_save, sender=settings.AUTH_USER_MODEL)
        @runner_signal
        @ignore_raw
        def my_signal_handler(sender, instance=None, created=False, **kwargs):
            ...
            return ...
    """

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        if not settings.DEPLOY_RUNNER:
            # Ignore signal handling for fixture loading
            return

        return self.f(*args, **kwargs)


ignore_raw = IgnoreRawDecorator
runner_signal = RunnerSignalDecorator
