```
{
  "url": "https://community.grafana.com/t/how-to-get-number-of-instances-of-multidimensional-alert/86150",
  "id": 86150,
  "slug": "how-to-get-number-of-instances-of-multidimensional-alert",
  "title": "How to get number of instances of multidimensional alert",
  "content": "<p>Alert list in <em>Stat</em> view mode shows number of Alert rules in selected state(s). I wonder if there is a way to show number of instances of multidimensional alert?</p>\n<p>I thought if I use empty custom grouping, it could work but unfortunately it does not. In <em>List</em> view mode with empty custom grouping, I see what I expected, ie. plain list, no grouping, and I would like in Stat view mode to see a number that corresponds to number of lines in the list.</p>\n<p>Thank you.</p>"
}
```

## Recommendations: How to get number of instances of multidimensional alert

- URL: https://community.grafana.com/t/how-to-get-number-of-instances-of-multidimensional-alert/86150
- Tags: Dashboarding, Transformations
- Summary: The writer asks for a way to display the number of instances of multidimensional alerts in Grafana.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member might suggest using a Transformations feature to achieve the desired result. Also, they may suggest using a table panel showing alerts instead of a Stat panel showing the number of alerts, as it might provide more useful information.

```
{
  "url": "https://community.grafana.com/t/generate-jwks-for-jwt-authentication/86171",
  "id": 86171,
  "slug": "generate-jwks-for-jwt-authentication",
  "title": "Generate JWKS for jwt authentication",
  "content": "<p>Hi, I\u2019m using Grafana 9.4.7 and I\u2019m trying to implement jwt authentication.<br>\nIs there an example on how to generate JWKS.json?<br>\nThis is my configuration file:</p>\n<pre><code class=\"lang-auto\">protocol = https\ndomain = my-ip\ncert_file = C:\\Program Files\\GrafanaLabs\\grafana\\etc\\grafana.crt\ncert_key = C:\\Program Files\\GrafanaLabs\\grafana\\etc\\grafana.key\ncookie_secure = true\ncookie_samesite = none\nallow_embedding = true\n[auth.jwt]\nenabled = true\nheader_name = X-JWT-Assertion\nemail_claim = sub\nusername_claim = sub\n</code></pre>\n<p>When I launch I obviously obtain the following error in the console:</p>\n<blockquote>\n<p>key set for jwt verification is not configured</p>\n</blockquote>"
}
```

## Recommendations: Generate JWKS for jwt authentication

- URL: https://community.grafana.com/t/generate-jwks-for-jwt-authentication/86171
- Tags: Auth, Plugins
- Summary: The user is trying to implement jwt authentication in Grafana 9.4.7 and needs help generating JWKS.json.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member can explain to the user that they need to generate a key pair and publish the public key as jwks_uri in the OpenID Connect metadata of the IdP, and then use the private key in Grafana's configuration file. They can also suggest using a library like node-jwks-rsa to simplify the process.

```
{
  "url": "https://community.grafana.com/t/how-to-calculate-weekly-montly-consumption-based-on-counter-status/86170",
  "id": 86170,
  "slug": "how-to-calculate-weekly-montly-consumption-based-on-counter-status",
  "title": "How to calculate weekly/montly consumption based on counter status",
  "content": "<p>There is time series with counter status (gas meter). How to calculate consumption for a certain period?<br>\n<img src=\"https://global.discourse-cdn.com/grafana/original/3X/2/d/2d78b84cf5fc4b78e7f72c5e9fdef087b9784b3c.png\" alt=\"counter\" data-base62-sha1=\"6ug7TMCrPrHwtVzjHwRCHrNQC7y\" width=\"181\" height=\"358\"></p>"
}
```

## Recommendations: How to calculate weekly/montly consumption based on counter status

- URL: https://community.grafana.com/t/how-to-calculate-weekly-montly-consumption-based-on-counter-status/86170
- Tags: Dashboarding, Transformations
- Summary: The post discusses how to calculate the consumption based on counter status in a certain period.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member can respond by suggesting the use of a time range selector for the period, and creating a transformation that calculates the difference between the counter values for the beginning and end of the selected period to obtain the consumption. The suggestion can include a relevant query or function documentation.

```
{
  "url": "https://community.grafana.com/t/using-json-parser-in-logql-with-special-characters/86165",
  "id": 86165,
  "slug": "using-json-parser-in-logql-with-special-characters",
  "title": "Using JSON parser in LogQL with special characters",
  "content": "<p>(topic deleted by author)</p>"
}
```

## Recommendations: Using JSON parser in LogQL with special characters

- URL: https://community.grafana.com/t/using-json-parser-in-logql-with-special-characters/86165
- Tags: Loki, Logging
- Summary: The author is having difficulty using the JSON parser in LogQL when dealing with special characters.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could suggest that the author try using single quotes instead of double quotes around the JSON query. Another suggestion may be to escape any special characters with a backslash.

```
{
  "url": "https://community.grafana.com/t/loki-alert-rule-configuration-of-time-range/86166",
  "id": 86166,
  "slug": "loki-alert-rule-configuration-of-time-range",
  "title": "Loki Alert Rule - configuration of time range",
  "content": "<p>I have Loki alert rules that should alert on the occurrence of certain even found in logs.<br>\nWhat should be the lookback time range in the alert configuration to ensure no instances of log events are missed.<br>\nFor example, if the alert rule is configured to be evaluated every 1m, should the lookback time range also be 1m or greater than 1m to account for delays in execution? Let\u2019s say the rule is configured to be evaluated every 60s but in actually it executed 61s after the prior execution, I\u2019m assuming that it would miss a log event for evaluation that happened 60.5 seconds ago if the lookback time range is 60s.<br>\nIs that assumption correct and if so, how to best decide the ideal lookback time range to ensure no log events are missed from evaluation?</p>"
}
```

## Recommendations: Loki Alert Rule - configuration of time range

- URL: https://community.grafana.com/t/loki-alert-rule-configuration-of-time-range/86166
- Tags: Loki, Logging, Transformations
- Summary: A user is seeking guidance on setting the lookback time range in Loki alert rules to ensure no instances of log events are missed.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could suggest setting the lookback time range to be slightly greater than the evaluation time, to account for potential delays in execution, and offer recommendations for determining the ideal range based on the specific system and data being analyzed. They could also provide tips on using transformations to filter data and improve the effectiveness of alert rules.

```
{
  "url": "https://community.grafana.com/t/overlapping-problem-with-status-history/86163",
  "id": 86163,
  "slug": "overlapping-problem-with-status-history",
  "title": "Overlapping Problem With Status History",
  "content": "<p>Hey, i want to show the sensor situation which is 0 or 1 but the problem is the results from a sensor are overlapping.</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/5/1/518e39326b68036db96ec51f6d5655b36a652a81.png\" data-download-href=\"/uploads/short-url/bDto17Yukrf1pL3Un9HsNAOKqDT.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/5/1/518e39326b68036db96ec51f6d5655b36a652a81_2_690x308.png\" alt=\"image\" data-base62-sha1=\"bDto17Yukrf1pL3Un9HsNAOKqDT\" width=\"690\" height=\"308\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/5/1/518e39326b68036db96ec51f6d5655b36a652a81_2_690x308.png, https://global.discourse-cdn.com/grafana/optimized/3X/5/1/518e39326b68036db96ec51f6d5655b36a652a81_2_1035x462.png 1.5x, https://global.discourse-cdn.com/grafana/original/3X/5/1/518e39326b68036db96ec51f6d5655b36a652a81.png 2x\" data-dominant-color=\"2B2223\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">1036\u00d7463 13.3 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>So when i get a data in 12.50 and 3 minutes later then they are overlapping. How can i fix it?</p>\n<p>Thanks</p>"
}
```

## Recommendations: Overlapping Problem With Status History

- URL: https://community.grafana.com/t/overlapping-problem-with-status-history/86163
- Tags: dashboards, panels, visualization types
- Summary: The user is facing a problem where the results from a sensor are overlapping on the dashboard.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could suggest using the "Staircase" option in the Display tab of the panel to avoid overlapping of results on the dashboard. Additionally, the member could guide the user to utilize the time range controls or set the resolution of the data source to avoid overlapping.

```
{
  "url": "https://community.grafana.com/t/alerts-migrated-to-unified-alerting-show-unhelpful-values/86162",
  "id": 86162,
  "slug": "alerts-migrated-to-unified-alerting-show-unhelpful-values",
  "title": "Alerts Migrated to Unified alerting show unhelpful values",
  "content": "<p>Hello all,</p>\n<p>I\u2019ve upgraded from v8.5.11 to v9.4.7 yesterday, and a lot of alerts were affected by the following:</p>\n<p>Example:</p>\n<pre><code class=\"lang-auto\">query: sum(logback_events_total{maintainer=\"team\",level=\"error\"})  by (service)\nalert condition: classic_conditions: diff(A) &gt; 0\n</code></pre>\n<p>Legacy alerting reports the following when an alert triggers</p>\n<pre><code class=\"lang-auto\">[[Alerting] Errors on the last 30s]\nValue {service=service_name}\n1\n</code></pre>\n<p>Unified alerting reports:</p>\n<pre><code class=\"lang-auto\">[[FIRING:1] Errors on the last 30s (id)]\n**Firing**\nValue: B0=1\nLabels:\n- alertname = Errors on the last 30s\n- grafana_folder = folder\n- rule_uid = id\n</code></pre>\n<p>Is this output with value: B0=1desired behaviour? As it would be very helpful for my team to continue to see the service name instead of B0. I managed to show it in a different part of the alert using {{ $values.B0.Labels.service }}, but ideally <code>Value</code> field should show inherited labels from the query if possible. I\u2019ve since had to roll back to legacy alerting.</p>"
}
```

## Recommendations: Alerts Migrated to Unified alerting show unhelpful values

- URL: https://community.grafana.com/t/alerts-migrated-to-unified-alerting-show-unhelpful-values/86162
- Tags: OnCall, Grafana, Dashboarding
- Summary: A user upgraded from v8.5.11 to v9.4.7 and alerts affected by Unified alerting show unhelpful values rather than the service name, despite providing the desired labels in the query.
- Friendly: Yes
- Concern: No
- Notes: A friendly response would be to suggest checking the configuration of the Unified Alerting and ensuring that the desired labels are specified in the query. Additionally, the user may want to consider posting their issue in the Grafana GitHub forum for more detailed feedback from the community.

```
{
  "url": "https://community.grafana.com/t/grafana-mariadb-mysql-time-issues/86158",
  "id": 86158,
  "slug": "grafana-mariadb-mysql-time-issues",
  "title": "Grafana MariaDB / MySQL time issues",
  "content": "<p>Dear All,</p>\n<p>I\u2019m having issues with fetching time series data from Mysql into my Grafana V9.3.6 dashboard.</p>\n<p>In my MariaDB table I have a field called: CurDate of type datetime. Each time a row is inserted this field is updated using UTC_TIMESTAMP(3). This stores the the time in UTC.</p>\n<p>My timezone is UTC +2:00, in the grafana dashboard this is also set up. The SQL server is also set to UTC +2:00</p>\n<p>I\u2019m running this query in grafana</p>\n<p>SELECT<br>\nCurDate AS \u201ctime\u201d,<br>\nVarValue AS \u2018Temperature\u2019<br>\nFROM log_data<br>\nWHERE<br>\n$__timeFilter(CurDate) AND VarId = 1</p>\n<p>Where grafana changes the timefilter to:</p>\n<p>CurDate BETWEEN FROM_UNIXTIME(1681982338) AND FROM_UNIXTIME(1681993138) AND VarId = 1</p>\n<p>1681993138 equals in UTC Thursday 20 April 2023 12:18:58 which corresponds to the time in my timezone of 14:18:58. Again in the database the values are stored in UTC, meaning if a value would be stored at the very same time this would be a timestamp of 2023-4-20 12:18:58</p>\n<p>The problem is that the FROM_UNIXTIME function is adding up again the 2 hours difference of the timezone. Now there is no data in my table as this is 2 hours in the future compared to the UTC timezone.</p>\n<p>Changing the time in the SQL database to actual time (+2 hours) solves the issue with grafana. But only if I substract 2 hours afterwards, like this:</p>\n<p>SELECT<br>\nDATE_SUB(CurDate, INTERVAL 2 HOUR)<br>\nVarValue AS \u2018Temperature\u2019<br>\nFROM log_data<br>\nWHERE<br>\n$__timeFilter(CurDate) AND VarId = 1</p>\n<p>However this gives issue when changing from summer to wintertime, and during the change from summer to wintertime I can have rows with identical timestamp in the table so I prefer to keep everything in UTC in my DB.</p>\n<p>How to properly fix this ?</p>"
}
```

## Recommendations: Grafana MariaDB / MySQL time issues

- URL: https://community.grafana.com/t/grafana-mariadb-mysql-time-issues/86158
- Tags: Database, Dashboarding, Transformations
- Summary: The user is having trouble with time series data from a MariaDB database in Grafana due to timezone issues.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member should recommend that the user adjust the timezone in their query to UTC rather than the SQL server timezone, and potentially adjust the timezone in the MariaDB table to UTC as well. They can also suggest using the DATE_ADD and DATE_SUB functions to adjust the timestamps as needed. Finally, they can recommend using Grafana's built-in timezone conversion functions in the dashboard to properly display the data to users in their desired timezone.

```
{
  "url": "https://community.grafana.com/t/i-would-like-to-use-the-status-history-feature-but-the-results-are-overlapping/86154",
  "id": 86154,
  "slug": "i-would-like-to-use-the-status-history-feature-but-the-results-are-overlapping",
  "title": "I would like to use the Status History feature, but the results are overlapping",
  "content": "<p>Hey, i am trying to show the status history from my park sensors. But the problem is, <strong>the results are overlapping when i want to show the results from last 24 hours The box, which is there to show the value if it is \u2018true\u2019 or \u2018false\u2019, is also thin and long</strong></p>\n<ul>\n<li>There is no problem when i show the last results from 1 Hours.</li>\n</ul>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/7/a/7a902b451c746c0d0667b8049c226702e37e36c9.png\" data-download-href=\"/uploads/short-url/huf8bNLoS7AutDS8uFprMLtZDHX.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/7/a/7a902b451c746c0d0667b8049c226702e37e36c9_2_690x327.png\" alt=\"image\" data-base62-sha1=\"huf8bNLoS7AutDS8uFprMLtZDHX\" width=\"690\" height=\"327\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/7/a/7a902b451c746c0d0667b8049c226702e37e36c9_2_690x327.png, https://global.discourse-cdn.com/grafana/optimized/3X/7/a/7a902b451c746c0d0667b8049c226702e37e36c9_2_1035x490.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/7/a/7a902b451c746c0d0667b8049c226702e37e36c9_2_1380x654.png 2x\" data-dominant-color=\"382127\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">1471\u00d7699 35.9 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>But when i want to show the last results from 24 Hours then they are overlapping also becoming thin and long.</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/d/6/d65f1120449111e13f0caa90b26ee54f6d6d1f65.png\" data-download-href=\"/uploads/short-url/uApRekyQaHGUqflcnJ6AGEoyWr3.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/d/6/d65f1120449111e13f0caa90b26ee54f6d6d1f65_2_690x240.png\" alt=\"image\" data-base62-sha1=\"uApRekyQaHGUqflcnJ6AGEoyWr3\" width=\"690\" height=\"240\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/d/6/d65f1120449111e13f0caa90b26ee54f6d6d1f65_2_690x240.png, https://global.discourse-cdn.com/grafana/optimized/3X/d/6/d65f1120449111e13f0caa90b26ee54f6d6d1f65_2_1035x360.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/d/6/d65f1120449111e13f0caa90b26ee54f6d6d1f65_2_1380x480.png 2x\" data-dominant-color=\"141619\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">1484\u00d7517 14.1 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>True text is too small to read. Whereas in the Status History documentation, the boxes are big enough, is there a way to set this? <a href=\"https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/status-history/\" rel=\"noopener nofollow ugc\">(The example of Status History documentation from Grafana)</a></p>\n<ul>\n<li>I <strong>want make them a small box, which i can read the result clearly for the last 12 Hours not only 1 hours.</strong>\n</li>\n</ul>\n<p>And also i want to see the last last valid information always until i get the new information from my sensor. Is there any way to make it?</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/b/a/baa1471d11a05563977a6ad67787fe563f03589d.png\" data-download-href=\"/uploads/short-url/qD0lqmP3TAFUnYuY0fLHLTEyaYt.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/b/a/baa1471d11a05563977a6ad67787fe563f03589d_2_690x197.png\" alt=\"image\" data-base62-sha1=\"qD0lqmP3TAFUnYuY0fLHLTEyaYt\" width=\"690\" height=\"197\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/b/a/baa1471d11a05563977a6ad67787fe563f03589d_2_690x197.png, https://global.discourse-cdn.com/grafana/optimized/3X/b/a/baa1471d11a05563977a6ad67787fe563f03589d_2_1035x295.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/b/a/baa1471d11a05563977a6ad67787fe563f03589d_2_1380x394.png 2x\" data-dominant-color=\"141819\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">1486\u00d7426 17.3 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>Thank you in advance for your help.</p>"
}
```

## Recommendations: I would like to use the Status History feature, but the results are overlapping

- URL: https://community.grafana.com/t/i-would-like-to-use-the-status-history-feature-but-the-results-are-overlapping/86154
- Tags: Dashboarding, Plugins, Visualizations
- Summary: The user is having difficulty with the status history feature in Grafana, specifically, the results are overlapping when they want to show the results from the last 24 hours.
- Friendly: Yes
- Concern: No
- Notes: The user may benefit from adjusting the size of the boxes for the status history feature. They could also try using a different visualization, such as the table panel to display the data more clearly. A friendly community member may also suggest checking the sensor data to ensure it is not providing overlapping information.

```
{
  "url": "https://community.grafana.com/t/repeat-panels-based-on-custom-defined-dashboard-variable/86149",
  "id": 86149,
  "slug": "repeat-panels-based-on-custom-defined-dashboard-variable",
  "title": "Repeat panels based on custom defined dashboard variable",
  "content": "<ul>\n<li>\n<p>What Grafana version and what operating system are you using?<br>\nGrafana v9.3.0</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve?<br>\nI\u2019ve created a custom dashboard variable <code>$queue</code> by using the following query:</p>\n</li>\n</ul>\n<pre><code class=\"lang-auto\">label_values({__name__=~\"redis_queue_.*\"},__name__)\n</code></pre>\n<p>The result of this query is a list of all metrics that start with the <code>redis_queue_</code>.</p>\n<p>This variable is a multi-select. What I want to do is to create a repeatable panel based on the following expression:</p>\n<pre><code class=\"lang-auto\">sum($queue)\n</code></pre>\n<ul>\n<li>\n<p><strong>How</strong> are you trying to achieve it?<br>\nI\u2019ve created a Time Series panel and applied said expression. I\u2019ve also configured repeat settings to horizontal, two per row.</p>\n</li>\n<li>\n<p>What happened?<br>\nWhen I select only one value from a dropdown, everything is fine. However, if I select multiple values, I get the following error:</p>\n</li>\n</ul>\n<pre><code class=\"lang-auto\">422: error when executing query=\"sum((redis_queue_messages|redis_queue_questions))\" on the time range (start=1681985985000, end=1681986885000, step=15000): cannot recognize \"|redis_queue_messages))\"; unparsed data: \"redis_queue_messages|redis_queue_questions))\"\n</code></pre>\n<ul>\n<li>What did you <strong>expect</strong> to happen?<br>\nEach panel should display a sum of values for each selected value from the <code>$queue</code> variable. In the case above, I was expecting to get two panels, each showing a sum of <code>redis_queue_messages</code> and <code>redis_queue_questions</code> separately.</li>\n</ul>\n<p>So, I need to find a way to repeat panels and do a sum per selected value, not of all values at once. How can I achieve this?</p>"
}
```

## Recommendations: Repeat panels based on custom defined dashboard variable

- URL: https://community.grafana.com/t/repeat-panels-based-on-custom-defined-dashboard-variable/86149
- Tags: Dashboarding, Panels, Variables
- Summary: The user is trying to create repeatable panels based on a custom defined dashboard variable, but receives an error when selecting multiple values.
- Friendly: Yes
- Concern: No
- Notes: One option to achieve this might be to create a query for each value selected in the variable, then display the results in separate panels. Another option could be to use a repetition variable in the panel query, so that each selected value is displayed in a separate panel.

```
{
  "url": "https://community.grafana.com/t/can-i-use-promtail-as-an-https-proxy-server/86145",
  "id": 86145,
  "slug": "can-i-use-promtail-as-an-https-proxy-server",
  "title": "Can I use Promtail as an HTTPS proxy server?",
  "content": "<p>I have a question about Promtail. I know I can use Promtail as an HTTP or GRPC server, but <strong>can I use Promtail as an HTTPS server?</strong></p>\n<p>My case: we\u2019re running a Promtail instance as a proxy server between Promtail clients (thousands of nodes) and Loki cluster. Currently, we use the following <code>loki_push_api</code> configuration</p>\n<pre><code class=\"lang-auto\">clients:\n- url: http://my.loki.server:3100/loki/api/v1/push\n  tenant_id: random\n\nscrape_configs:\n- job_name: loki_push_api\n  loki_push_api:\n    server:\n      http_listen_port: 3100\n    use_incoming_timestamp: true\n</code></pre>\n<p>The thing is that we want to add one more client and one more scrape config to support both HTTP and HTTPS for security reasons, something like</p>\n<pre><code class=\"lang-auto\">clients:\n- url: http://my.loki.server:3100/loki/api/v1/push\n  tenant_id: random\n- url: https://my.loki.server:3101/loki/api/v1/push #let's suppose we're running 2 distributor instances, HTTP and HTTPS under the same hostname, different ports\n  tenant_id: random_tls\n\nscrape_configs:\n- job_name: loki_push_api\n  loki_push_api:\n    server:\n      http_listen_port: 3100\n    use_incoming_timestamp: true\n- job_name: loki_push_api_https\n  loki_push_api:\n    server:\n      http_listen_port: 3101\n      http_tls_config:\n        cert_file: /etc/ssl/certs/promtail/cert.pem\n        key_file: /etc/ssl/certs/promtail/key.pem\n    use_incoming_timestamp: true\n</code></pre>\n<p>I didn\u2019t test it, but I don\u2019t think this will work, because there is no such config option for Promtail</p>\n<blockquote>\n<p>Note the <code>server</code> configuration is the same as <a href=\"https://grafana.com/docs/loki/latest/clients/promtail/configuration/#server\" rel=\"noopener nofollow ugc\">server</a>.</p>\n</blockquote>\n<blockquote>\n<p>The server block configures Promtail\u2019s behavior as an HTTP server.</p>\n</blockquote>\n<p>My first question of this thread: <strong>does Promtail\u2019s server configuration support HTTPS?</strong></p>\n<p>If not, then my second question would be: <strong>does Promtail\u2019s server configuration support gRPC with SSL/TLS?</strong> Something like</p>\n<pre><code class=\"lang-auto\">clients:\n- url: http://my.loki.server:3100/loki/api/v1/push\n  tenant_id: random\n- url: https://my.loki.server:3101/loki/api/v1/push #let's suppose we're running 2 distributor instances, HTTP and HTTPS under the same hostname, different ports\n  tenant_id: random\n\nscrape_configs:\n- job_name: loki_push_api\n  loki_push_api:\n    server:\n      http_listen_port: 3100\n    use_incoming_timestamp: true\n- job_name: loki_push_api_grpc\n  loki_push_api:\n    server:\n      grpc_listen_port: 3101\n      grpc_tls_config:\n        cert_file: /etc/ssl/certs/promtail/cert.pem\n        key_file: /etc/ssl/certs/promtail/key.pem\n    use_incoming_timestamp: true\n</code></pre>\n<p>Also, my third question which is kind of an off-topic: H<strong>ow can I point to one particular client in my <code>scrape_config</code> I want to use?</strong></p>"
}
```

## Recommendations: Can I use Promtail as an HTTPS proxy server?

- URL: https://community.grafana.com/t/can-i-use-promtail-as-an-https-proxy-server/86145
- Tags: `Loki`, `HTTPS`, `Promtail`, `Security`
- Summary: The user is asking if it is possible to use Promtail as an HTTPS proxy server to support both HTTP and HTTPS for security reasons, and if not, if it supports gRPC with SSL/TLS.
- Friendly: Yes
- Concern: No
- Notes: A community member could suggest alternative solutions or workarounds for the user's use case, explain the technical limitations, or provide insight on the feasibility of the ideas presented in the post. They could also offer resources such as links to documentation or related discussions.

```
{
  "url": "https://community.grafana.com/t/setup-time-range-pv-power-from-6am-to-9pm-yesterday/86143",
  "id": 86143,
  "slug": "setup-time-range-pv-power-from-6am-to-9pm-yesterday",
  "title": "Setup time range pv power from 6am to 9pm yesterday",
  "content": "<p>Hi All,</p>\n<p>I\u2019m new here and I try to setup a dashboard for my PV.<br>\nI\u2019m struggeling with a panel which should show me the PV power from yesterday from 6am to 9pm and the same for the actual day.<br>\nI think it\u2019s easy, but I dont get it\u2026</p>\n<p>Thanks a lot\u2026<br>\n<div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/b/1/b1cec64bf82095d6b6f0070b39e4c23a6da5bb06.jpeg\" data-download-href=\"/uploads/short-url/pmXwxkty4hI8AsjX8gWLNWRmOxw.jpeg?dl=1\" title=\"grafana\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/b/1/b1cec64bf82095d6b6f0070b39e4c23a6da5bb06_2_690x407.jpeg\" alt=\"grafana\" data-base62-sha1=\"pmXwxkty4hI8AsjX8gWLNWRmOxw\" width=\"690\" height=\"407\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/b/1/b1cec64bf82095d6b6f0070b39e4c23a6da5bb06_2_690x407.jpeg, https://global.discourse-cdn.com/grafana/optimized/3X/b/1/b1cec64bf82095d6b6f0070b39e4c23a6da5bb06_2_1035x610.jpeg 1.5x, https://global.discourse-cdn.com/grafana/original/3X/b/1/b1cec64bf82095d6b6f0070b39e4c23a6da5bb06.jpeg 2x\" data-dominant-color=\"242F2A\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">grafana</span><span class=\"informations\">1213\u00d7716 70.7 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>"
}
```

## Recommendations: "Setup time range pv power from 6am to 9pm yesterday"

- URL: https://community.grafana.com/t/setup-time-range-pv-power-from-6am-to-9pm-yesterday/86143
- Tags: Dashboarding, Panels, Time Range
- Summary: User is struggling to display PV power for a specific time range in a panel and is seeking help.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could provide guidance on setting a specified time range for a panel in Grafana, and suggest using the Time Range feature to select a custom time range for the data to be displayed. Additionally, they could recommend checking documentation on Panels and Dashboarding in Grafana for further assistance.

```
{
  "url": "https://community.grafana.com/t/gauges-wont-snap-into-place/86141",
  "id": 86141,
  "slug": "gauges-wont-snap-into-place",
  "title": "Gauges won't snap into place",
  "content": "<p>I\u2019m trying to add some gauges to my PV system monitoring dashboard. I\u2019m having an issue where the new gauge won\u2019t snap to the correct place in the dashboard. There is visibly room but Grafana won\u2019t place the gauge where I drag it but offers to slip it into a different row, see the examples here.</p>\n<p><img src=\"https://global.discourse-cdn.com/grafana/original/3X/0/c/0cc954c0de35ecd95875cfbe2446c9829d889ada.png\" alt=\"image\" data-base62-sha1=\"1P74VtHFIqzpd5uUn9p3cPCexlM\" width=\"490\" height=\"496\"><br>\n<img src=\"https://global.discourse-cdn.com/grafana/original/3X/a/9/a9d3834e1aca5926a66e79a59d20bbf4c9af4598.png\" alt=\"image\" data-base62-sha1=\"oelR7DNItOO1sKrodE7DuQi8K6c\" width=\"474\" height=\"480\"></p>\n<p>My guess is that there is something occupying those grid positions in the second and third line which Grafana avoids. How can I see what it is? There is one panel to the right, but moving that won\u2019t help. In fact, it looks like the whole bottom right corner of the dashboard is off limits and nothing can be dragged there.</p>"
}
```

## Recommendations: "Gauges won't snap into place"

- URL: https://community.grafana.com/t/gauges-wont-snap-into-place/86141
- Tags: Dashboarding, Panels
- Summary: The user is having an issue where new gauges won't snap to the correct places in their dashboard, and is looking for a solution.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member might suggest checking if there are any hidden panels or visualizations taking up space in the dashboard, or checking the settings to make sure the grid is properly aligned. They may also suggest trying to drag the gauge to a different spot and see if that helps it snap into place, or using a different type of visualization.

```
{
  "url": "https://community.grafana.com/t/need-some-input-on-a-complicated-collection/86140",
  "id": 86140,
  "slug": "need-some-input-on-a-complicated-collection",
  "title": "Need some input on a complicated collection",
  "content": "<p>Hello everyone,</p>\n<p>I am currently debating between different tools to migrate our In-house monolith software that is responsible for collecting metric data (and other things) from over 10000 network devices.</p>\n<p>One of the key points we need to be able to do is chained lookups. I found a nice post explaining this in the following link that will explain what I\u2019m talking about: <a href=\"https://github.com/prometheus/snmp_exporter/issues/405\" class=\"inline-onebox\" rel=\"noopener nofollow ugc\">Support chained lookups \u00b7 Issue #405 \u00b7 prometheus/snmp_exporter \u00b7 GitHub</a></p>\n<p>I am not looking for an answer on how to do this collection, I just need a direction to documentation to make sure that this is something that can be done in a modern and robust way, for example python scripts that can be part of CI/CD pipeline etc etc.</p>\n<p>From what I understand, I need an SNMP exporter configuration file to collect specific OIDs. Then add a job to scrape the results of this configuration file and produce graphs.</p>\n<p>But how do you abstract all this to apply it to multiple devices/indexes at once?<br>\nA qos snmp question will generally contain the interface index, the queue number, the direction and the metric name. So X interfaces * 2 directions * 1-8 queue numbers * 16ish metrics is over 1000 metric points.</p>\n<p>Can you do this kind of chained lookup using the SNMP exporter configuration file? Is there another way?</p>\n<p>Any ideas or information about similar implementations will be highly appreciated.</p>"
}
```

## Recommendations: Need some input on a complicated collection

- URL: https://community.grafana.com/t/need-some-input-on-a-complicated-collection/86140
- Tags: Mimir, Prometheus, SNMP, Python, CI/CD
- Summary: The author seeks guidance in migrating their monolithic system for collecting metric data from network devices, specifically chained lookups, and whether SNMP exporter configuration file can be used to apply this to multiple devices, indexes at once.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could suggest exploring Mimir or Prometheus for collecting metric data from network devices and Python for member functionalities. The member could also suggest using CI/CD pipelines to automate the process and refer to related resources for additional guidance.
