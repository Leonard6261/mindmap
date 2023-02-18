from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Connection(models.Model):
    from_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='connections_from')
    to_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='connections_to')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.from_node} -> {self.to_node}"
