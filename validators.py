from datetime import datetime

import unter_pb2 as pb


class ValidationError(Exception):
    pass


def _validate_ride(request: pb.StartRideRequest|pb.EndRideRequest):
    if not request.id:
        raise ValidationError('missing id')

    if request.time.ToDatetime() > datetime.now():
        raise ValidationError('time is in the future')


def validate_start(request: pb.StartRideRequest):
    _validate_ride(request)

    if request.kind not in (pb.KIND_REGULAR, pb.KIND_SHARED):
        raise ValidationError('unknown kind')

    if not request.driver_id:
        raise ValidationError('missing driver')


def validate_end(request: pb.EndRideRequest):
    _validate_ride(request)

    if request.distance <= 0:
        raise ValidationError('bad distance')
