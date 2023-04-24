args=Namespace(topic=None)
Got 10 topics
```
{
  "url": "https://community.grafana.com/t/promtail-container-crashes-with-an-error-failed-to-make-file-target-manager-too-many-open-files/86248",
  "id": 86248,
  "slug": "promtail-container-crashes-with-an-error-failed-to-make-file-target-manager-too-many-open-files",
  "title": "Promtail container crashes with an error \"failed to make file target manager: too many open files\"",
  "content": "<p>Hello  , I face with a permanent crashing of prom tail\u2019s container with an error which is \u201cfailed to make file target manager: too many open files\u201d. I use official docker compose file.</p>\n<p>Additionally I added ulimits parameter , but it didn\u2019t help .</p>\n<p>version: \u201c3\u201d</p>\n<p>networks:<br>\nloki:</p>\n<p>services:<br>\npromtail:<br>\nimage: grafana/promtail:2.8.0<br>\nvolumes:<br>\n- /var/log:/var/log<br>\ncommand: -config.file=/etc/promtail/config.yml<br>\nulimits:<br>\nnofile:<br>\nsoft: 65536<br>\nhard: 65536<br>\nnetworks:<br>\n- loki<br>\nError from a container:<br>\nlevel=error ts=2023-04-20T21:50:49.989724713Z caller=main.go:170 msg=\u201cerror creating promtail\u201d error=\u201cfailed to make file target manager: too many open files\u201d</p>\n<p>I appreciate any pieces of advice !<br>\nThank you !</p>"
}
```


## Recommendations: (Promtail container crashes with an error "failed to make file target manager: too many open files")

- URL: https://community.grafana.com/t/promtail-container-crashes-with-an-error-failed-to-make-file-target-manager-too-many-open-files/86248
- Tags: Docker, Loki, Infrastructure
- Summary: The Prometheus tail (Promtail) container crashes with an error "failed to make file target manager: too many open files", even after setting the ulimits parameter. 
- Friendly: Yes
- Concern: No
- Notes: The user has already taken steps to address this issue by adding the ulimits parameter, but to no avail. One possible solution could be to increase the nofile limit beyond the currently set value of 65536. Another suggestion would be to check if there are any memory leaks caused by the container. Additionally, the user can also check if there are any other host processes that are currently using up all the available file descriptors.
```
{
  "url": "https://community.grafana.com/t/how-to-edit-query-for-wan-upload/86360",
  "id": 86360,
  "slug": "how-to-edit-query-for-wan-upload",
  "title": "How to edit query for WAN upload",
  "content": "<p>Hi,<br>\nI\u2019m new to grafana and have absolutely no experience in building queries so please pardon me if this question is dumb.<br>\nI\u2019ve set up grafana+prometheus to monitor my router (Fritzbox). There is a github project called \u201cfritz_exporter\u201d which extracts the data from the router via upnp.<br>\nI\u2019ve downloaded a dashboard which monitors all the data I need, so far so good.</p>\n<p>Now I would like to set an alarm when my upload falls under a certain value (e.g. 3Mbyte/s) for 15 minutes or so. The goal is to check if my online backup is complete so I can shut down my NAS. Yes, I know asking the backup software via API would be so much more ideal but afaik Synology Drive Share Sync does not give you such an option.</p>\n<p>So I\u2019m able to set an alarm but it also fires  when my download rate is under 3Mbyte/s. I just want to monitor the upload rate.</p>\n<p>How can I edit the query to achieve that?</p>\n<p>Thanks is advance!</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/a/5/a57db4f0395eb4d2a49d5018700b84eae5c67315.png\" data-download-href=\"/uploads/short-url/nC06HQu9Zf3cHPRBXMlbfMIVb2R.png?dl=1\" title=\"grafana\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/a/5/a57db4f0395eb4d2a49d5018700b84eae5c67315_2_690x465.png\" alt=\"grafana\" data-base62-sha1=\"nC06HQu9Zf3cHPRBXMlbfMIVb2R\" width=\"690\" height=\"465\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/a/5/a57db4f0395eb4d2a49d5018700b84eae5c67315_2_690x465.png, https://global.discourse-cdn.com/grafana/optimized/3X/a/5/a57db4f0395eb4d2a49d5018700b84eae5c67315_2_1035x697.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/a/5/a57db4f0395eb4d2a49d5018700b84eae5c67315_2_1380x930.png 2x\" data-dominant-color=\"202227\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">grafana</span><span class=\"informations\">1384\u00d7933 101 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<ul>\n<li>\n<p>What Grafana version and what operating system are you using?<br>\n9.4.7</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve?<br>\nSetting up an alarm when Upload is below a certain value.</p>\n</li>\n<li>\n<p><strong>How</strong> are you trying to achieve it?<br>\nUsing fritz_exporter from Github.</p>\n</li>\n<li>\n<p>What happened?<br>\nI\u2019m unable to separate Upload and Download.</p>\n</li>\n<li>\n<p>What did you <strong>expect</strong> to happen?<br>\nAlerting only when Upload is below certain value.</p>\n</li>\n<li>\n<p>Can you copy/paste the configuration(s) that you are having problems with?</p>\n</li>\n</ul>\n<ul>\n<li>\n</li>\n</ul>\n<ul>\n<li>Did you receive any errors in the Grafana UI or in related logs? If so, please tell us <strong>exactly</strong> what they were.</li>\n</ul>\n<ul>\n<li>\n</li>\n</ul>\n<ul>\n<li>Did you follow any online instructions? If so, what is the URL?<br>\nCan not find examples for this query.</li>\n</ul>"
}
```


## Recommendations: How to edit query for WAN upload

- URL: https://community.grafana.com/t/how-to-edit-query-for-wan-upload/86360
- Tags: dashboarding, prometheus, transformations, monitoring
- Summary: The poster is trying to set an alarm when their upload falls under a certain value by editing the query in a Grafana dashboard, but is unsure how to do so.
- Friendly: yes
- Concern: no
- Notes: A friendly community member could suggest using the query editor in the Grafana dashboard to modify the query to only include the upload rate metric. Alternatively, they could recommend looking at the documentation for the fritz_exporter to see if there are any filters or flags that can be used to extract only the upload data. Finally, they could suggest using a separate monitoring tool, such as Nagios, to achieve this functionality.
```
{
  "url": "https://community.grafana.com/t/beginner-needs-tool-to-help-himself-panel-with-no-data/86362",
  "id": 86362,
  "slug": "beginner-needs-tool-to-help-himself-panel-with-no-data",
  "title": "Beginner needs tool to help himself: Panel with no data",
  "content": "<p>Hi,</p>\n<p>I\u2019m looking to learn how to help my self on Grafana. I recently tested this great tool out to monitor some of our servers, tested some dashboards, buildt one by trial-and-error by myself and now decided to dive deeper into it.</p>\n<p>I moved from a test server enviroment to prodution recently and also adopted nginx rveerse proxy, https with certbot. server is running with ufw activated. Now I have done the whole migration, last issue is with my custom dashboard: I have some panels that dont show data anymore. this is mostly some checks for RAM and HDD Space usage and one uptime panel.</p>\n<p>Now all but one panel worked before and the last one that never worked I would also like to know how to fix. I have read about using inspector several times but couldnt figure out how to do it properly. For now I give one example for you guys to better understand my panel issue:</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/e/c/eca473ee484ddaeccb4cd64b00de7896ae00e942.png\" data-download-href=\"/uploads/short-url/xLr1lbUVpMQYaxEabde8OxjN2xQ.png?dl=1\" title=\"grafik\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/c/eca473ee484ddaeccb4cd64b00de7896ae00e942_2_626x500.png\" alt=\"grafik\" data-base62-sha1=\"xLr1lbUVpMQYaxEabde8OxjN2xQ\" width=\"626\" height=\"500\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/c/eca473ee484ddaeccb4cd64b00de7896ae00e942_2_626x500.png, https://global.discourse-cdn.com/grafana/optimized/3X/e/c/eca473ee484ddaeccb4cd64b00de7896ae00e942_2_939x750.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/e/c/eca473ee484ddaeccb4cd64b00de7896ae00e942_2_1252x1000.png 2x\" data-dominant-color=\"1C1F22\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">grafik</span><span class=\"informations\">1833\u00d71462 281 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>this relay show no RAM usage anymore. The alias is correct according to prometheus targets. This might be one of the most easier fixes since I can only see several reasons:</p>\n<ul>\n<li>the alias is not defined yet and I dont know how/where to do it properly. I remember when entering the alias name in code query it appeared/autocompleted but on the new envioment nothing happens so this is my hot guess.</li>\n<li>firewall is blocking something that did not got blocked in test env without fw</li>\n</ul>\n<p>maybe you have a good hint or even better a tutorial where I can figure out how to fix this by myself with the inspector, would be great to be able to fix this in the future by myself <img src=\"https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12\" title=\":slight_smile:\" class=\"emoji\" alt=\":slight_smile:\" loading=\"lazy\" width=\"20\" height=\"20\"></p>\n<p>best regards!</p>"
}
```


## Recommendations: Beginner needs tool to help himself: Panel with no data

- URL: https://community.grafana.com/t/beginner-needs-tool-to-help-himself-panel-with-no-data/86362
- Tags: Dashboarding, Loki, OnCall, Phlare
- Summary: A beginner Grafana user is seeking advice to fix issues with custom dashboard panels that stopped showing data after migrating to a new environment.
- Friendly: Yes
- Concern: No
- Notes: The user is seeking help to troubleshoot issues with the custom dashboard panels that stopped showing data after migration. The post seems friendly and does not contain any inappropriate content. A community member can suggest the following steps: 
  - Check if data is still available in the data source
  - Verify that the query is correctly set up
  - Check if there are any errors in the logs
  - Use Inspector to inspect the panel, including the data source, query, and visualization settings.
```
{
  "url": "https://community.grafana.com/t/loki-is-deleting-logs-of-killed-deleted-containers-before-the-retention-policy/86355",
  "id": 86355,
  "slug": "loki-is-deleting-logs-of-killed-deleted-containers-before-the-retention-policy",
  "title": "Loki is deleting logs of killed/deleted containers before the retention policy",
  "content": "<ul>\n<li>\n<p>What loki version and what operating system are you using?<br>\nloki:2.6.1</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve?<br>\nkeep logs in the selected namespace for configurable time</p>\n</li>\n<li>\n<p><strong>How</strong> are you trying to achieve it?<br>\nwe have configured limits_config</p>\n</li>\n<li>\n<p>What happened?<br>\nLogs are correctly retained for the containers that are still running.<br>\nIf the user manually kills or deletes a container these logs are deleted before the configured retain policy.</p>\n</li>\n<li>\n<p>What did you <strong>expect</strong> to happen?<br>\nAll logs linked to containers matching particular selectors should be kept by Loki until the retain policy.</p>\n</li>\n<li>\n<p>Can you copy/paste the configuration(s) that you are having problems with?<br>\nwe are using loki-grafana-agent-operator and helmfiles</p>\n</li>\n</ul>\n<p>loki:<br>\ncommonConfig:<br>\nreplication_factor: 1<br>\nstorage:<br>\ntype: \u2018filesystem\u2019<br>\nrulerConfig:<br>\nstorage:<br>\ntype: local<br>\nauth_enabled: false<br>\nlimits_config:<br>\nretention_period: 168h<br>\nretention_stream:<br>\n- selector: \u2018{namespace=\u201cgate\u201d}\u2019<br>\npriority: 1<br>\nperiod: {{ .Values.logging.retentionPeriod | default \u201c744h\u201d }}<br>\nmonitoring:<br>\nselfMonitoring:<br>\nlokiCanary:<br>\nenabled: false<br>\nglobal:<br>\ndnsService: rke2-coredns-rke2-coredns<br>\nsingleBinary:<br>\npersistence:<br>\nstorageClass: {{ .Values.storage.usage.logs }}</p>\n<ul>\n<li>\n<p>Did you receive any errors in the Grafana UI or in related logs? If so, please tell us <strong>exactly</strong> what they were.<br>\nNo errors</p>\n</li>\n<li>\n<p>Did you follow any online instructions? If so, what is the URL?<br>\nyes but this part is not covered:  <a href=\"https://grafana.com/docs/loki/latest/operations/storage/retention/\" class=\"inline-onebox\" rel=\"noopener nofollow ugc\">Retention | Grafana Loki documentation</a></p>\n</li>\n</ul>"
}
```


## Recommendations: Loki is deleting logs of killed/deleted containers before the retention policy

- URL: https://community.grafana.com/t/loki-is-deleting-logs-of-killed-deleted-containers-before-the-retention-policy/86355
- Tags: Loki, Docker, Logging
- Summary: The post describes an issue where logs linked to containers are deleted before the configured retention policy in Loki.
- Friendly: Yes
- Concern: No
- Notes: The user can try adding the `block_request` flag to the loki helm chart values file to prevent deletion of logs, and can also check if there are any background processes or jobs that could be deleting the logs. If the issue persists, they could consider opening a bug report on the Loki GitHub repository or asking for help on the Grafana community forum.
```
{
  "url": "https://community.grafana.com/t/grafana-alert-manager-webhook-integration-does-not-support-mtls/86353",
  "id": 86353,
  "slug": "grafana-alert-manager-webhook-integration-does-not-support-mtls",
  "title": "Grafana Alert Manager - Webhook integration does not support mTLS",
  "content": "<ul>\n<li>\n<p>What Grafana version and what operating system are you using?<br>\nA - Version - 9.4.7</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve?<br>\nA - Grafana Alert Manager Webhook Configuration using mTLS.</p>\n</li>\n<li>\n<p><strong>How</strong> are you trying to achieve it?<br>\nA - Using Grafana Alert Manager</p>\n</li>\n<li>\n<p>What happened?<br>\nA - Grafana Alert Manager does not support mTLS configuration.</p>\n</li>\n<li>\n<p>What did you <strong>expect</strong> to happen?<br>\nA - Support for mTLS configuration or some other workaround. My Webhook destination is mTLS enabled and hence it cannot be called without client certs. There is no way of configuring Client certs for Grafana Webhook Integration. Is there some workaround with which this can be achieved?</p>\n</li>\n<li>\n<p>Can you copy/paste the configuration(s) that you are having problems with?<br>\nA - NA</p>\n</li>\n<li>\n<p>Did you receive any errors in the Grafana UI or in related logs? If so, please tell us <strong>exactly</strong> what they were.<br>\nA - NA</p>\n</li>\n<li>\n<p>Did you follow any online instructions? If so, what is the URL?<br>\nA - NA</p>\n</li>\n</ul>"
}
```


## Recommendations: Grafana Alert Manager - Webhook integration does not support mTLS

- URL: https://community.grafana.com/t/grafana-alert-manager-webhook-integration-does-not-support-mtls/86353 
- Tags: Grafana, OnCall, Auth, Plugins 
- Summary: The user is trying to configure Grafana Alert Manager webhook with mTLS but it is not supported and is looking for a workaround.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member can reply by suggesting the user to try using an external proxy, like nginx, to terminate the mTLS and forward the request to Grafana. They can also provide a link to documentation on how to configure Grafana with a reverse proxy for added security features. Additionally, they can suggest submitting a feature request to the Grafana team for adding support for mTLS configuration in their webhook integration.
```
{
  "url": "https://community.grafana.com/t/panel-csv-plugin/86352",
  "id": 86352,
  "slug": "panel-csv-plugin",
  "title": "Panel/ CSV Plugin",
  "content": "<p>Hello,<br>\nI have csv as a data source and trying to visualize it as time series or another graph but it can only visualize as a table. What is the problem? What should I change in the query ?</p>\n<p>THANK YOU!!<br>\n<div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/b/5/b5db9aedb3883f07801293fa3b2091ebacf3e036.png\" data-download-href=\"/uploads/short-url/pWMVieSXR9KnYs6NG85DdqUByse.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/b/5/b5db9aedb3883f07801293fa3b2091ebacf3e036_2_690x492.png\" alt=\"image\" data-base62-sha1=\"pWMVieSXR9KnYs6NG85DdqUByse\" width=\"690\" height=\"492\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/b/5/b5db9aedb3883f07801293fa3b2091ebacf3e036_2_690x492.png, https://global.discourse-cdn.com/grafana/optimized/3X/b/5/b5db9aedb3883f07801293fa3b2091ebacf3e036_2_1035x738.png 1.5x, https://global.discourse-cdn.com/grafana/original/3X/b/5/b5db9aedb3883f07801293fa3b2091ebacf3e036.png 2x\" data-dominant-color=\"171A1E\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">1224\u00d7874 44 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div><br>\n<div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/e/b/eb9e7d529d7d88a259b1fa5814e5eb9f646d09a5.png\" data-download-href=\"/uploads/short-url/xCnLBy57wjFgxSZfgAD7DsYKt0x.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/b/eb9e7d529d7d88a259b1fa5814e5eb9f646d09a5_2_690x376.png\" alt=\"image\" data-base62-sha1=\"xCnLBy57wjFgxSZfgAD7DsYKt0x\" width=\"690\" height=\"376\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/b/eb9e7d529d7d88a259b1fa5814e5eb9f646d09a5_2_690x376.png, https://global.discourse-cdn.com/grafana/optimized/3X/e/b/eb9e7d529d7d88a259b1fa5814e5eb9f646d09a5_2_1035x564.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/e/b/eb9e7d529d7d88a259b1fa5814e5eb9f646d09a5_2_1380x752.png 2x\" data-dominant-color=\"1A1D22\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">1681\u00d7918 74.2 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>"
}
```


## Recommendations: (Panel/ CSV Plugin)

- URL: https://community.grafana.com/t/panel-csv-plugin/86352
- Tags: datasources, transformations
- Summary: The user is having trouble visualizing data from a CSV data source in Grafana.
- Friendly: Yes
- Concern: No
- Notes: It would be helpful to know what the user's query currently looks like, so that specific suggestions can be given. One option would be to use a transformation to convert the CSV data to a more usable format, such as JSON, before visualization. Another option would be to adjust the current query to properly format and group the data for visualization as a time series or other graph type.
```
{
  "url": "https://community.grafana.com/t/webvitals-sample-dashboard-with-otel-as-the-collector-type/86347",
  "id": 86347,
  "slug": "webvitals-sample-dashboard-with-otel-as-the-collector-type",
  "title": "Webvitals Sample Dashboard with Otel as the Collector Type",
  "content": "<ul>\n<li>\n<p>What Grafana version and what operating system are you using?<br>\nv9.4.3</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve?<br>\nCreating Webvitals Dashboard with Otel as Backend</p>\n</li>\n<li>\n<p><strong>How</strong> are you trying to achieve it?<br>\nWe are using Otel to retrieve values from our browser agent and send it to mimir .</p>\n</li>\n<li>\n<p>What happened?<br>\nWe are looking for some inspirations on inputs related to representing Webvitals values.<br>\nAny one who has created these kind of dashboards will be very helpfull.</p>\n</li>\n<li>\n<p>What did you <strong>expect</strong> to happen?</p>\n</li>\n<li>\n<p>Can you copy/paste the configuration(s) that you are having problems with?<br>\nI dont have any problems , i am looking for some inspirations.</p>\n</li>\n<li>\n<p>Did you receive any errors in the Grafana UI or in related logs? If so, please tell us <strong>exactly</strong> what they were.</p>\n</li>\n<li>\n<p>Did you follow any online instructions? If so, what is the URL?</p>\n</li>\n</ul>"
}
```


## Recommendations: Webvitals Sample Dashboard with Otel as the Collector Type

- URL: https://community.grafana.com/t/webvitals-sample-dashboard-with-otel-as-the-collector-type/86347
- Tags: dashboarding, mimir, loki, datasources, web-vitals
- Summary: The poster is trying to create a webvitals dashboard with Otel as a backend and is looking for inspiration.
- Friendly: Yes
- Concern: No
- Notes: The poster seems to be asking for help and inspiration rather than reporting an issue, so a friendly community member could suggest looking at the Loki logging data source or using Mimir with Prometheus and provide dashboards for web vitals as examples. Additionally, the poster could consider using the Web Vitals plugin for Grafana to create their dashboard.
```
{
  "url": "https://community.grafana.com/t/query-with-multiple-group-by-time/86345",
  "id": 86345,
  "slug": "query-with-multiple-group-by-time",
  "title": "Query with multiple GROUP BY time",
  "content": "<p>Hi all,</p>\n<p>Trying to figure this out for the last few days but couldn\u2019t get it to work so wondering if anyone could help me out.</p>\n<p>I have data from a sensor about my hourly energy usage (from Home Assistant through Influx). Only the sensor doesn\u2019t have hourly data points, but it add\u2019s each data point within a given hour and resets at the end to 0. So there are multiple data points per hour and the last one being the total value.</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f.png\" data-download-href=\"/uploads/short-url/fhzMrTXQ2oRu14AgcA1E5KUeMRF.png?dl=1\" title=\"Screenshot 2023-04-24 at 10.37.58\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_689x419.png\" alt=\"Screenshot 2023-04-24 at 10.37.58\" data-base62-sha1=\"fhzMrTXQ2oRu14AgcA1E5KUeMRF\" width=\"689\" height=\"419\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_689x419.png, https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_1033x628.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_1378x838.png 2x\" data-dominant-color=\"1D2024\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">Screenshot 2023-04-24 at 10.37.58</span><span class=\"informations\">2598\u00d71578 328 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>Now I can view the total hourly energy usage by SELECTING the max(value) and GROUP BY time(1h). This works fine. Only now I want the group the already grouped hourly data points again to each day and calculate the total sum so I know how much I\u2019ve used each day. Only I have no idea how to group a query multiple times?</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529.png\" data-download-href=\"/uploads/short-url/xFZX8uJHxhJk4Ym2B4b3q8tujFf.png?dl=1\" title=\"Screenshot 2023-04-24 at 10.38.15\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_690x424.png\" alt=\"Screenshot 2023-04-24 at 10.38.15\" data-base62-sha1=\"xFZX8uJHxhJk4Ym2B4b3q8tujFf\" width=\"690\" height=\"424\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_690x424.png, https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_1035x636.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_1380x848.png 2x\" data-dominant-color=\"1C1F24\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">Screenshot 2023-04-24 at 10.38.15</span><span class=\"informations\">2602\u00d71600 330 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>Would appreciate any help!</p>"
}
```


## Recommendations: Query with multiple GROUP BY time

- URL: https://community.grafana.com/t/query-with-multiple-group-by-time/86345
- Tags: influx, database, transformations, dashboarding, panels
- Summary: The user is trying to group hourly data points by the hour and by day to calculate daily energy usage using Influx and is seeking help to group a query multiple times.
- Friendly: Yes
- Concern: No
- Notes: The user has provided enough information to understand the issue and is seeking help politely. An approach to solve the problem with Influx is to use nested queries, performing the first grouping by the hour and then group the results of that query by the day. It is also possible to do this in Grafana by creating a variable that groups by the hour and another by the day, and creating a panel with one row for each day that summarizes the hourly data.
```
{
  "url": "https://community.grafana.com/t/all-created-dashboard-and-alerts-disappeared-help/86308",
  "id": 86308,
  "slug": "all-created-dashboard-and-alerts-disappeared-help",
  "title": "All created dashboard and alerts disappeared - HELP",
  "content": "<p>(topic deleted by author)</p>"
}
```


## Recommendations: All created dashboard and alerts disappeared - HELP

- URL: https://community.grafana.com/t/all-created-dashboard-and-alerts-disappeared-help/86308
- Tags: dashboarding
- Summary: The user is reporting that all their created dashboards and alerts have disappeared, and they are seeking help.
- Friendly: Neutral
- Concern: No
- Notes: It seems like the user accidentally deleted their dashboards and alerts. A friendly community member could suggest checking the trash folder. They could also suggest setting up backups in the future to prevent data loss.
```
{
  "url": "https://community.grafana.com/t/how-to-change-grafana-html-title-version-9-0-3-in-dashboard-page-not-a-mainpage/86337",
  "id": 86337,
  "slug": "how-to-change-grafana-html-title-version-9-0-3-in-dashboard-page-not-a-mainpage",
  "title": "How to change Grafana Html title? Version 9.0.3 in dashboard page (not a mainpage)",
  "content": "<p><strong>Please avoid posting in the Grafana parent category. Whenever possible choose a subcategory.</strong></p>\n<p>in Grafana version 9.0.3 How to change Grafana Title?<br>\neven change the html [.apptitle] will rollback again<br>\nMight be have build file?<br>\nPlease help me</p>\n<p>THANK YOU!!</p>\n<p>~ the grafana team</p>"
}
```


## Recommendations: How to change Grafana Html title? Version 9.0.3 in dashboard page (not a mainpage)

- URL: https://community.grafana.com/t/how-to-change-grafana-html-title-version-9-0-3-in-dashboard-page-not-a-mainpage/86337
- Tags: Grafana, Dashboarding
- Summary: The post asks for help on changing the title of the dashboard page in Grafana version 9.0.3.
- Friendly: Yes
- Concern: No
- Notes: A friendly response could provide the user with a possible solution to their problem. This could include using the "page_title" variable in the dashboard JSON settings or using a text panel to display a custom title. It could also suggest checking if any plugins or custom CSS files are interfering with the title display. Additionally, a reminder to the user to post their queries in the appropriate subcategory could be included.
