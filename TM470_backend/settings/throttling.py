from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class LoginUserThrottle(UserRateThrottle):
    rate = '100/hour'


class LoginAnonThrottle(AnonRateThrottle):
    rate = '100/hour'
