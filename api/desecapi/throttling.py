from rest_framework import throttling
from rest_framework.settings import api_settings

from desecapi import metrics


class ScopedRatesThrottle(throttling.ScopedRateThrottle):
    """
    Like DRF's ScopedRateThrottle, but supports several rates per scope, e.g. for burst vs. sustained limit.
    """
    def parse_rate(self, rates):
        return [super(ScopedRatesThrottle, self).parse_rate(rate) for rate in rates]

    def allow_request(self, request, view):
        # We can only determine the scope once we're called by the view.
        self.scope = getattr(view, self.scope_attr, None)

        # If a view does not have a `throttle_scope` always allow the request
        if not self.scope:
            return True

        # Determine the allowed request rate as we normally would during
        # the `__init__` call.
        self.rate = self.get_rate()
        if self.rate is None:
            return True

        self.now = self.timer()
        self.num_requests, self.duration = zip(*self.parse_rate(self.rate))
        self.key = self.get_cache_key(request, view)
        self.history = {key: [] for key in self.key}
        self.history.update(self.cache.get_many(self.key))

        for num_requests, duration, key in zip(self.num_requests, self.duration, self.key):
            history = self.history[key]
            # Drop any requests from the history which have now passed the
            # throttle duration
            while history and history[-1] <= self.now - duration:
                history.pop()
            if len(history) >= num_requests:
                # Prepare variables used by the Throttle's wait() method that gets called by APIView.check_throttles()
                self.num_requests, self.duration, self.key, self.history = num_requests, duration, key, history
                response = self.throttle_failure()
                metrics.get('desecapi_throttle_failure').inc()
                return response
            self.history[key] = history
        return self.throttle_success()

    def throttle_success(self):
        for key in self.history:
            self.history[key].insert(0, self.now)
        self.cache.set_many(self.history, max(self.duration))
        return True

    # Override the static attribute of the parent class so that we can dynamically apply override settings for testing
    @property
    def THROTTLE_RATES(self):
        return api_settings.DEFAULT_THROTTLE_RATES

    def get_cache_key(self, request, view):
        key = super().get_cache_key(request, view)
        return [f'{key}_{duration}' for duration in self.duration]
