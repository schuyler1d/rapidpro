# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-16 16:23
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("channels", "0002_auto_20180716_1623"),
        ("contacts", "0001_initial"),
        ("orgs", "0001_initial"),
        ("msgs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="channellog",
            name="msg",
            field=models.ForeignKey(
                help_text="The message that was sent",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_logs",
                to="msgs.Msg",
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="channel",
            field=models.ForeignKey(
                help_text="The channel on which this event took place",
                on_delete=django.db.models.deletion.PROTECT,
                to="channels.Channel",
                verbose_name="Channel",
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="contact",
            field=models.ForeignKey(
                help_text="The contact associated with this event",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_events",
                to="contacts.Contact",
                verbose_name="Contact",
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="contact_urn",
            field=models.ForeignKey(
                help_text="The contact URN associated with this event",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_events",
                to="contacts.ContactURN",
                verbose_name="URN",
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="org",
            field=models.ForeignKey(
                help_text="The org this event is connected to",
                on_delete=django.db.models.deletion.PROTECT,
                to="orgs.Org",
                verbose_name="Org",
            ),
        ),
        migrations.AddField(
            model_name="channelcount",
            name="channel",
            field=models.ForeignKey(
                help_text="The channel this is a daily summary count for",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="counts",
                to="channels.Channel",
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channels_channel_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channels_channel_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="org",
            field=models.ForeignKey(
                blank=True,
                help_text="Organization using this channel",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channels",
                to="orgs.Org",
                verbose_name="Org",
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                help_text="The channel this channel is working on behalf of",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="channels.Channel",
            ),
        ),
        migrations.AddField(
            model_name="alert",
            name="channel",
            field=models.ForeignKey(
                help_text="The channel that this alert is for",
                on_delete=django.db.models.deletion.PROTECT,
                to="channels.Channel",
                verbose_name="Channel",
            ),
        ),
        migrations.AddField(
            model_name="alert",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channels_alert_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="alert",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channels_alert_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="alert",
            name="sync_event",
            field=models.ForeignKey(
                help_text="The sync event that caused this alert to be sent (if any)",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="channels.SyncEvent",
                verbose_name="Sync Event",
            ),
        ),
        migrations.AlterIndexTogether(name="channelcount", index_together=set([("channel", "count_type", "day")])),
    ]
