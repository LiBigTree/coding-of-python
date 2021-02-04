# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We
# sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#
#
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True
def sleep_in(weekday, vacation):
    if weekday is False:
        return True
    if weekday is True:
        if vacation is True:
            return True
        if vacation is False:
            return False


def sleep_in_v2(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    # This can be shortened to: return(not weekday or vacation)
