from django.db import models

class DemotionQueue(models.Model):
    """data model for demotion queue

    """

    action = models.CharField(max_length=55)
    admin = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="admin_demotion_queues")
    approver_one = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="approver_one_demotion_queues")