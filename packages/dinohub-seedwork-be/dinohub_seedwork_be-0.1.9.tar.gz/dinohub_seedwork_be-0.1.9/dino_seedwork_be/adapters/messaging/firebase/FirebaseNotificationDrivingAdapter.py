import json

from firebase_admin import messaging
from returns.future import FutureFailure, FutureResult, FutureSuccess

from dino_seedwork_be.adapters.messaging.firebase.AbstractUserNotificationPushDrivingAdapter import \
    UserNotificationPushDrivingAdapter

app = messaging.firebase_admin.initialize_app()

__all__ = ["FirebaseNotificationDrivingAdapter", "app"]


class FirebaseNotificationDrivingAdapter(UserNotificationPushDrivingAdapter):
    def push_to_device(
        self, content: dict, type: str, device_token: str
    ) -> FutureResult:
        try:
            message = messaging.Message(
                data={"type": type, "content": json.dumps(content)}, token=device_token
            )

            response = messaging.send(message)

            return FutureSuccess(response)
        except Exception as error:
            return FutureFailure(error)
