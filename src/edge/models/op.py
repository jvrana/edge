from django.db import models
from edge.models import Fragment


class Operation(models.Model):
    class Meta:
        app_label = "edge"

    RECOMBINATION = 'Recombination'
    CRISPR_CUT = 'CRISPR Cut'
    CRISPR_NICK = 'CRISPR Nick'
    TRANSPOSON = 'Transposon integration'

    type = models.CharField(max_length=64,
                            choices=((RECOMBINATION, 'Recombination'),
                                     (CRISPR_CUT, 'CRISPR Cut'),
                                     (CRISPR_NICK, 'CRISPR Nick'),
                                     (TRANSPOSON, 'Transposon integration')))
    notes = models.TextField(null=True, blank=True)
    fragment = models.ForeignKey(Fragment)
