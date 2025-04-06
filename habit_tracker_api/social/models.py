from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL

class Friendship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} follows {self.friend.username}"

    class Meta:
        unique_together = ('user', 'friend')
