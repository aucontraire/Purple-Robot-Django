from django.conf.urls import patterns, url

from views import ingest_payload_print, log_event, pr_home, pr_by_probe, \
    pr_by_user, test_report, test_details_json, tests_by_user, \
    create_export_job, fetch_export_file, tests_all, ingest_payload, config, \
    pr_device, pr_add_group, pr_add_device, pr_configurations, pr_configuration, \
    pr_device_probe

urlpatterns = patterns('',
    url(r'^config$', config, name='pr_config'),
    url(r'^configurations$', pr_configurations, name='pr_configurations'),
    url(r'^configuration/(?P<config_id>.+)$', pr_configuration, name='pr_configuration'),
    url(r'^print$', ingest_payload_print, name='ingest_payload_print'),
    url(r'^log$', log_event, name='log_event'),
    url(r'^home$', pr_home, name='pr_home'),
    url(r'^add_group$', pr_add_group, name='pr_add_group'),
    url(r'^group/(?P<group_id>.+)/add_device$', pr_add_device, name='pr_add_device'),
    url(r'^device/(?P<device_id>.+)/(?P<probe_name>.+)$', pr_device_probe, name='pr_device_probe'),
    url(r'^device/(?P<device_id>.+)$', pr_device, name='pr_device'),
    url(r'^probes$', pr_by_probe, name='pr_by_probe'),
    url(r'^user$', pr_by_user, name='pr_by_user'),
    url(r'^test/(?P<slug>.+)$', test_report, name='test_report'),
    url(r'^tests/(?P<slug>.+)/detail.json$', test_details_json, name='test_details_json'),
    url(r'^tests/(?P<user_id>.+)$', tests_by_user, name='tests_by_user'),
    url(r'^export$', create_export_job, name='create_export_job'),
    url(r'^export_files/(?P<job_pk>.+)$', fetch_export_file, name='fetch_export_file'),
    url(r'^tests/$', tests_all, name='tests_all'),
    url(r'^$', ingest_payload, name='ingest_payload'),
)
