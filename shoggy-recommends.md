Namespace(topic=None, search=None, replies=False, tags=False)
## Recommendations: Configuring alerts on panel with multiple Variables

- URL: https://community.grafana.com/t/configuring-alerts-on-panel-with-multiple-variables/86386
- Tags: dashboards, variables
- Summary: The poster is experiencing issues configuring alerts on a panel with multiple variables, as the alert marker is showing up on the same point in every graph for each host name.
- Friendly: Yes
- Concern: No
- Notes: It appears that the poster is simply looking for a solution to a configuration issue. A friendly community member could suggest exploring the use of different alert rules for each hostname, or looking into creating multiple panels with separate alerts for each variable selection.


```
{
  "url": "https://community.grafana.com/t/configuring-alerts-on-panel-with-multiple-variables/86386",
  "id": 86386,
  "slug": "configuring-alerts-on-panel-with-multiple-variables",
  "title": "Configuring alerts on panel with multiple Variables",
  "content": "<p>I have a dashboard with variables set so I can select different host names, for example, and when selecting those host names switches the graph for the corresponding host name.</p>\n<p>I setup an alert by clicking on the panel \u2192 Edit \u2192 Alert (tab). Now, the problem seems that the alert is working, but it\u2019s showing the alert marker at the same point in every single graph for each host name, which doesn\u2019t help me at all because I have no idea which hostname\u2019s graph data generated the alert.</p>\n<p>Is this just not possible to do? I\u2019d like to have the alert for every single individual hostname when I select it from the drop-down menu.</p>"
}
```


## Recommendations: How to text wrap the content in table

- URL: https://community.grafana.com/t/how-to-text-wrap-the-content-in-table/86382
- Tags: Dashboards, Transformations
- Summary: The poster is asking how to wrap text in a table in the latest version of Grafana.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could suggest using the 'Cell Style' option in the table panel configuration to customize the cell's width and overflow settings. They could also suggest using a markdown table instead of a Grafana table if the formatting is not critical.


```
{
  "url": "https://community.grafana.com/t/how-to-text-wrap-the-content-in-table/86382",
  "id": 86382,
  "slug": "how-to-text-wrap-the-content-in-table",
  "title": "How to text wrap the content in table",
  "content": "<p>How to text wrap the content in table ? i am using the latest version</p>"
}
```


## Recommendations: Webvitals Sample Dashboard with Otel as the Collector Type

- URL: https://community.grafana.com/t/webvitals-sample-dashboard-with-otel-as-the-collector-type/86347
- Tags: dashboards, Mimir, Loki, OnCall
- Summary: The poster is asking for input on creating a Webvitals Dashboard with Otel as Backend data source.
- Friendly: Yes
- Concern: No
- Notes: It would be helpful to ask for more specific information on what data the poster is looking to display on the dashboard, and whether any specific Loki or OnCall integrations are needed. Additionally, the Pyroscope tag could be added if the poster is interested in utilizing continuous profiling for code optimization.


```
{
  "url": "https://community.grafana.com/t/webvitals-sample-dashboard-with-otel-as-the-collector-type/86347",
  "id": 86347,
  "slug": "webvitals-sample-dashboard-with-otel-as-the-collector-type",
  "title": "Webvitals Sample Dashboard with Otel as the Collector Type",
  "content": "<ul>\n<li>\n<p>What Grafana version and what operating system are you using?<br>\nv9.4.3</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve?<br>\nCreating Webvitals Dashboard with Otel as Backend</p>\n</li>\n<li>\n<p><strong>How</strong> are you trying to achieve it?<br>\nWe are using Otel to retrieve values from our browser agent and send it to mimir .</p>\n</li>\n<li>\n<p>What happened?<br>\nWe are looking for some inspirations on inputs related to representing Webvitals values.<br>\nAny one who has created these kind of dashboards will be very helpfull.</p>\n</li>\n<li>\n<p>What did you <strong>expect</strong> to happen?</p>\n</li>\n<li>\n<p>Can you copy/paste the configuration(s) that you are having problems with?<br>\nI dont have any problems , i am looking for some inspirations.</p>\n</li>\n<li>\n<p>Did you receive any errors in the Grafana UI or in related logs? If so, please tell us <strong>exactly</strong> what they were.</p>\n</li>\n<li>\n<p>Did you follow any online instructions? If so, what is the URL?</p>\n</li>\n</ul>"
}
```


## Recommendations: Query with multiple GROUP BY time

- URL: https://community.grafana.com/t/query-with-multiple-group-by-time/86345
- Tags: Datasource, Database, Transformations
- Summary: The user is trying to group hourly data points to each day to calculate the total sum but doesn't know how to group a query multiple times.
- Friendly: Yes
- Concern: No
- Notes: The user can achieve the desired result by selecting `max(value)` and group by `time(1h)` to view the total hourly energy usage. Then, the user can use subqueries and group by `time($interval)` and time range to group the hourly data points again to each day and calculate the total sum. In the subquery, group by `time($interval)` and use the `sum()` aggregation function to calculate the sum. Then, use another query to group the results by `time($interval)` and use the `sum()` aggregation function to calculate the total sum for each day. Finally, the user can use transformations, such as `groupBy` and `sum`, to format the data in the desired way.


```
{
  "url": "https://community.grafana.com/t/query-with-multiple-group-by-time/86345",
  "id": 86345,
  "slug": "query-with-multiple-group-by-time",
  "title": "Query with multiple GROUP BY time",
  "content": "<p>Hi all,</p>\n<p>Trying to figure this out for the last few days but couldn\u2019t get it to work so wondering if anyone could help me out.</p>\n<p>I have data from a sensor about my hourly energy usage (from Home Assistant through Influx). Only the sensor doesn\u2019t have hourly data points, but it add\u2019s each data point within a given hour and resets at the end to 0. So there are multiple data points per hour and the last one being the total value.</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f.png\" data-download-href=\"/uploads/short-url/fhzMrTXQ2oRu14AgcA1E5KUeMRF.png?dl=1\" title=\"Screenshot 2023-04-24 at 10.37.58\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_689x419.png\" alt=\"Screenshot 2023-04-24 at 10.37.58\" data-base62-sha1=\"fhzMrTXQ2oRu14AgcA1E5KUeMRF\" width=\"689\" height=\"419\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_689x419.png, https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_1033x628.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/6/b/6b1d42e6a41fb489d19b24dec681d4fdd834834f_2_1378x838.png 2x\" data-dominant-color=\"1D2024\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">Screenshot 2023-04-24 at 10.37.58</span><span class=\"informations\">2598\u00d71578 328 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>Now I can view the total hourly energy usage by SELECTING the max(value) and GROUP BY time(1h). This works fine. Only now I want the group the already grouped hourly data points again to each day and calculate the total sum so I know how much I\u2019ve used each day. Only I have no idea how to group a query multiple times?</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529.png\" data-download-href=\"/uploads/short-url/xFZX8uJHxhJk4Ym2B4b3q8tujFf.png?dl=1\" title=\"Screenshot 2023-04-24 at 10.38.15\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_690x424.png\" alt=\"Screenshot 2023-04-24 at 10.38.15\" data-base62-sha1=\"xFZX8uJHxhJk4Ym2B4b3q8tujFf\" width=\"690\" height=\"424\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_690x424.png, https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_1035x636.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/e/c/ec0720a9eb4f4afceabc63e8fd0c380a65295529_2_1380x848.png 2x\" data-dominant-color=\"1C1F24\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">Screenshot 2023-04-24 at 10.38.15</span><span class=\"informations\">2602\u00d71600 330 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>Would appreciate any help!</p>"
}
```


## Recommendations: All created dashboard and alerts disappeared - HELP

- URL: https://community.grafana.com/t/all-created-dashboard-and-alerts-disappeared-help/86308
- Tags: Dashboards, OnCall
- Summary: The user is reporting that all of their created dashboards and alerts have disappeared.
- Friendly: Neutral
- Concern: No
- Notes: As there is no content in the post and it has been deleted by the author, there is not much that can be done. However, if they repost with more information, a friendly community member could suggest possible solutions such as checking the database or version control, or asking if anyone else who has access to the system deleted the dashboards and alerts.


```
{
  "url": "https://community.grafana.com/t/all-created-dashboard-and-alerts-disappeared-help/86308",
  "id": 86308,
  "slug": "all-created-dashboard-and-alerts-disappeared-help",
  "title": "All created dashboard and alerts disappeared - HELP",
  "content": "<p>(topic deleted by author)</p>"
}
```


Total processed: 5
