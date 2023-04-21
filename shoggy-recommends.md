args=Namespace(topic=None)
Got 8 topics
```
{
  "url": "https://community.grafana.com/t/columnname-based-on-positive-negative/86243",
  "id": 86243,
  "slug": "columnname-based-on-positive-negative",
  "title": "Columnname based on positive/negative",
  "content": "<p>Hello!</p>\n<p>I display how long it takes, to complete charging a battery to 90%.<br>\nWhen it discharging, I calculate how long it takes to 10%.</p>\n<p>I would like to display now the text to the time:<br>\n90% reached in xxx<br>\n10% reached in xxx</p>\n<p>This is my stat display:<br>\n<img src=\"https://global.discourse-cdn.com/grafana/original/3X/8/6/864df678feb15da9439ccec5ecfdefffa190fc0d.png\" alt=\"image\" data-base62-sha1=\"ja70XIbbuFWGN7QGwLUvVNNTwrb\" width=\"310\" height=\"154\"></p>\n<p>This is my flux query:</p>\n<pre><code class=\"lang-auto\">import \"timezone\"\noption location = timezone.location(name: \"Europe/Vienna\")\n\nfrom(bucket: \"bucket\")\n  |&gt; range(start: -5m, stop: v.timeRangeStop)\n  |&gt; filter(fn: (r) =&gt; r[\"_measurement\"] == \"PV\")\n  |&gt; filter(fn: (r) =&gt; r[\"Wechselrichter\"] == \"Alle\")\n  |&gt; filter(fn: (r) =&gt; r[\"Speicher\"] == \"Alle\")\n  |&gt; filter(fn: (r) =&gt; r[\"_field\"] == \"Lade/Entladeleistung\" or  r[\"_field\"] == \"SoC\")\n  |&gt; filter(fn: (r) =&gt; r[\"_value\"] &lt; 20000 and r[\"_value\"] &gt; -20000)\n  |&gt; aggregateWindow(every: 5m, fn: last, createEmpty: false)\n  |&gt; pivot(rowKey: [\"_time\"], columnKey: [\"_field\"], valueColumn: \"_value\")\n  |&gt; map(fn: (r) =&gt; ({ r with \n  Ladezeit: if r[\"Lade/Entladeleistung\"] &gt; 300.0 \n    then \n      ((40500.0 - (45000.0 * r[\"SoC\"] / 100.0)) / r[\"Lade/Entladeleistung\"]) * 60.0 * 60.0\n    else if r[\"Lade/Entladeleistung\"] &lt; -300.0 \n    then\n     (((45000.0 * r[\"SoC\"] / 100.0) -4500.0) / r[\"Lade/Entladeleistung\"] * -1.0) * 60.0 * 60.0\n    else\n     0.0\n    })\n  )\n  |&gt; keep(columns: [\"Ladezeit\"])\n  |&gt; yield(name: \"last\")\n</code></pre>\n<p>Can I change in the flux the column name?</p>"
}
```


## Recommendations: Columnname based on positive/negative

- URL: https://community.grafana.com/t/columnname-based-on-positive-negative/86243
- Tags: transformations, dashboards, variables
- Summary: The user wants to change the names of columns in their Grafana stat display.
- Friendly: Yes
- Concern: No
- Notes: A community member could suggest creating a new panel and renaming the columns in the query, or using the rename function in the Flux query to change the column display names. It might also be helpful to provide further information on the desired outcome for the column name changes.
```
{
  "url": "https://community.grafana.com/t/problems-with-log-fields-in-loki-using-promtail-cri-o-json/86242",
  "id": 86242,
  "slug": "problems-with-log-fields-in-loki-using-promtail-cri-o-json",
  "title": "Problems with log fields in Loki using promtail (cri-o/json)",
  "content": "<p>Hi,<br>\nThe promtail is not sent to Loki the fields in a parsed way, so in Loki\u2019s UI I can\u2019t search for a specific field.<br>\n<div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/grafana/original/3X/1/1/114e6ba4247d236b6bd4ad74ff639201ca69607d.png\" data-download-href=\"/uploads/short-url/2t68bK141oLxKP2aF1NcfxI2xvD.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/grafana/optimized/3X/1/1/114e6ba4247d236b6bd4ad74ff639201ca69607d_2_690x158.png\" alt=\"image\" data-base62-sha1=\"2t68bK141oLxKP2aF1NcfxI2xvD\" width=\"690\" height=\"158\" srcset=\"https://global.discourse-cdn.com/grafana/optimized/3X/1/1/114e6ba4247d236b6bd4ad74ff639201ca69607d_2_690x158.png, https://global.discourse-cdn.com/grafana/optimized/3X/1/1/114e6ba4247d236b6bd4ad74ff639201ca69607d_2_1035x237.png 1.5x, https://global.discourse-cdn.com/grafana/optimized/3X/1/1/114e6ba4247d236b6bd4ad74ff639201ca69607d_2_1380x316.png 2x\" data-dominant-color=\"202326\"><div class=\"meta\">\n<svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">1771\u00d7408 78 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg>\n</div></a></div></p>\n<p>I did the installation on loki+promtail using the loki-stack chart.<br>\nI already tried to add a json in the pipelineStages but nothing changed. (promtail).</p>\n<p>Could someone help me to make this work?</p>"
}
```


## Recommendations: Problems with log fields in Loki using promtail (cri-o/json)

- URL: https://community.grafana.com/t/problems-with-log-fields-in-loki-using-promtail-cri-o-json/86242
- Tags: Loki, Mimir, logging, prometheus, Phlare
- Summary: The poster is having difficulty searching for a specific field in Loki's UI due to promtail not sending fields in a parsed way.
- Friendly: Yes
- Concern: No
- Notes: It may be helpful to suggest that the poster double-check their pipelineStages configuration in promtail and verify that the json parsing rule is correctly set up. Additionally, they may want to consider using a Loki-specific log driver in place of promtail, such as Loki Docker Driver, to simplify the logging process.
```
{
  "url": "https://community.grafana.com/t/while-configuring-grafana-im-facing-error-in-dashboard-it-says-e-replace-is-not-a-function/86241",
  "id": 86241,
  "slug": "while-configuring-grafana-im-facing-error-in-dashboard-it-says-e-replace-is-not-a-function",
  "title": "While configuring grafana , im facing error in dashboard , it says \"e.replace is not a function\"",
  "content": "<ul>\n<li>\n<p>What Grafana version and what operating system are you using?  v7.3.4</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve? Viewing data metrics</p>\n</li>\n<li>\n<p><strong>How</strong> are you trying to achieve it? Using Prometheus</p>\n</li>\n<li>\n<p>What happened? While configuring dashboard it throws an error</p>\n</li>\n<li>\n<p>What did you <strong>expect</strong> to happen? Work</p>\n</li>\n<li>\n<p>Can you copy/paste the configuration(s) that you are having problems with?</p>\n</li>\n</ul>\n<p>Error Updating Option: e.replace is not a function</p>\n<ul>\n<li>\n<p>Did you receive any errors in the Grafana UI or in related logs? If so, please tell us <strong>exactly</strong> what they were.</p>\n</li>\n<li>\n<p>Did you follow any online instructions? If so, what is the URL?</p>\n</li>\n</ul>"
}
```


## Recommendations: While configuring grafana , im facing error in dashboard , it says "e.replace is not a function"

- URL: https://community.grafana.com/t/while-configuring-grafana-im-facing-error-in-dashboard-it-says-e-replace-is-not-a-function/86241
- Tags: Dashboarding, Grafana, Prometheus
- Summary: The user is facing an error "e.replace is not a function" while configuring a dashboard in Grafana to view data metrics with Prometheus.
- Friendly: Yes
- Concern: No
- Notes: The issue seems to be related to a problem with an option in the Grafana UI. One potential solution is to check the JSON configuration for errors or try resetting the option. Other users in the community have suggested checking the versions of Grafana and Prometheus to ensure compatibility.
```
{
  "url": "https://community.grafana.com/t/logical-operators-in-annotation-filters/86240",
  "id": 86240,
  "slug": "logical-operators-in-annotation-filters",
  "title": "Logical Operators in Annotation filters",
  "content": "<ul>\n<li>\n<p>What Grafana version and what operating system are you using?<br>\nv9.1.8 on Windows10</p>\n</li>\n<li>\n<p><strong>What</strong> are you trying to achieve?<br>\nLets say there are annotations like:<br>\na1 \u2192 {\u2026, tags: [\u201cmetadata\u201d, \u201csensor1\u201d, \u201ctemp\u201d]}<br>\na2 \u2192 {\u2026, tags:[\u201cmetadata\u201d, \u201csensor2\u201d, \u201ctemp\u201d]}<br>\na3 \u2192 {\u2026, tags:[\u201cmetadata\u201d, \u201csensor3\u201d, \u201ctemp\u201d]}<br>\na4 \u2192 {\u2026, tags:[\u201cmetadata\u201d, \u201csensor4\u201d, \u201cdepth\u201d]}<br>\na5 \u2192 {\u2026, tags:[\u201coutliers\u201d, \u201csensor1\u201d]}<br>\na6-&gt; {\u2026, tags:[\u201coutliers\u201d, \u201csensor2\u201d]}<br>\nI only want to display annotations a1, a2.</p>\n</li>\n<li>\n<p><strong>How</strong> are you trying to achieve it?<br>\nAdd an annotation filter (for grafana built-in annotations), that filters annotations based on tags (as already implemented), BUT also allow logical operators.<br>\nHow would I create a filter to only show annotations with the tags \u201cmetadata\u201d AND \u201ctemp\u201d AND (\u201csensor1\u201d OR \u201csensor2\u201d)    (But not \u201csensor3\u201d and not \u201coutliers\u201d, e.g.)?</p>\n</li>\n</ul>"
}
```


## Recommendations: Logical Operators in Annotation filters

- URL: https://community.grafana.com/t/logical-operators-in-annotation-filters/86240
- Tags: Dashboarding, Transformations
- Summary: The poster is asking for help on how to add a filter to annotations to only show annotations that have certain tags, while also allowing logical operators.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could explain that to show annotations a1 and a2 with tags "metadata" and "temp" AND either "sensor1" OR "sensor2", the annotation filter could be set to"(tags='metadata' AND tags='temp') AND (tags='sensor1' OR tags='sensor2')".
```
{
  "url": "https://community.grafana.com/t/unnamed-columns-in-my-csv/86234",
  "id": 86234,
  "slug": "unnamed-columns-in-my-csv",
  "title": "Unnamed columns in my CSV",
  "content": "<p>Hello, I used the CSV plugin to visualize my data in .CSV but when I look at the columns, one of them is \u201cUnnamed: 1959\u201d.</p>\n<p><img src=\"https://global.discourse-cdn.com/grafana/original/3X/c/2/c2cf8864d89cdf8305ed54a9aa0bfa99838cbec9.png\" alt=\"grafa\" data-base62-sha1=\"rNngvkPN7oa3w0P0aUISuueJbXr\" width=\"174\" height=\"222\"></p>\n<p>Does it mean there are more columns but Grafana can\u2019t display them ?</p>"
}
```


## Recommendations: Unnamed columns in my CSV

- URL: https://community.grafana.com/t/unnamed-columns-in-my-csv/86234
- Tags: Dashboards, Plugins, Transformations
- Summary: The user is using the CSV plugin to visualize data but noticed that one of the columns is named "Unnamed: 1959" and is looking for an explanation.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member could suggest that the user check the CSV file to ensure that there are no hidden or empty columns present, and to try renaming or removing the problematic column to see if there are any changes in the visualization. They could also suggest exploring the Transformations functionality in Grafana to see if it can help address any potential data issues.
```
{
  "url": "https://community.grafana.com/t/table-column-filter-issue/86230",
  "id": 86230,
  "slug": "table-column-filter-issue",
  "title": "Table column filter issue",
  "content": "<p>Hi everyone,</p>\n<p>I have a simple table that displays some information that the user may need to filter.<br>\nColumn filters looked great but by default, it won\u2019t select any of the filtered items:</p>\n<p>For instance, I filter the column on \u2018brosse\u2019 and see the filter list with checkboxes disabled:<br>\n<img src=\"https://global.discourse-cdn.com/grafana/original/3X/e/3/e3273034d4cf9fdeffb6f64eb0f32b53bae40d30.png\" alt=\"2023-04-21 13_21_38-Ventes Client - Dashboards - Grafana and 10 more pages - Personal - Microsoft\u200b E\" data-base62-sha1=\"wpultn39B2vrVb4zINjrEyvlhPa\" width=\"635\" height=\"461\"></p>\n<p>The fact that the checkboxes are disabled by default means that the filter won\u2019t be applied unless I tick every item.<br>\nTo me that\u2019s counter-productive to the principle of a filter, especially since people are used to the way it works in Excel, where filtered items will be selected by default (I mean that\u2019s the point of filtering).</p>\n<p>Is there a way to achiever this that I\u2019m missing?</p>\n<p>I think the default behaviour should be to select (tick) all filtered items by default, and provide a \u201ctoggle selection\u201d option at the bottom so users can quickly refine the filtered items.</p>"
}
```


## Recommendations: Table column filter issue

- URL: https://community.grafana.com/t/table-column-filter-issue/86230
- Tags: Dashboarding, Plugins
- Summary: The user is having issues with the default behavior of column filters in a table panel and wants to know if there is a way to select all filtered items by default.
- Friendly: Yes
- Concern: No
- Notes: One possible solution is to use the "Filter by Name" option in the "Table" tab of the panel editor. Another option is to use a plugin such as "Filter Panel" or "Table Panel Filter" for more advanced filtering capabilities.
```
{
  "url": "https://community.grafana.com/t/set-prometheus-version-in-datasource-yaml-configuration-not-working/86229",
  "id": 86229,
  "slug": "set-prometheus-version-in-datasource-yaml-configuration-not-working",
  "title": "Set Prometheus version in datasource YAML configuration not working",
  "content": "<p>I\u2019m trying to install Grafana (version v9.4.7) in Kubernetes with the <a href=\"https://github.com/grafana/helm-charts/blob/main/charts/grafana/values.yaml\" rel=\"noopener nofollow ugc\">Grafana Helm chart</a>.</p>\n<p>I have setup the Prometheus datasource in the Helm chart values:</p>\n<pre><code class=\"lang-yaml\">datasources:\n  datasources.yaml:\n    apiVersion: 1\n    datasources:\n      - name: Prometheus\n        type: prometheus\n        url: http://prometheus:9090\n        access: proxy\n        jsonData:\n          timeout: 120\n          queryTimeout: 2m\n          httpMethod: GET\n          manageAlerts: true\n          prometheusType: Prometheus\n          prometheusVersion: \"&gt; 2.40.x\"\n</code></pre>\n<p>The problem is that <code>prometheusVersion</code> variable (found in documentation <a href=\"https://grafana.com/docs/grafana/latest/datasources/prometheus/#provisioning-example\" rel=\"noopener nofollow ugc\">here</a>) does not set the Prometheus version:</p>\n<p><img src=\"https://global.discourse-cdn.com/grafana/original/3X/b/a/ba02f84b5b828b147a834ce12ae2c9d09720fcfd.png\" alt=\"image\" data-base62-sha1=\"qxxaH1UVU0kSpovvuh64IlISgKF\" width=\"401\" height=\"132\"></p>\n<p>And when provisioned with the Helm chart all changes to the datasource are gone after pod restart.</p>\n<p>Is it not possible to set the Prometheus version in provision YAML configuration or am I doing something wrong?</p>"
}
```


## Recommendations: Set Prometheus version in datasource YAML configuration not working

- URL: https://community.grafana.com/t/set-prometheus-version-in-datasource-yaml-configuration-not-working/86229
- Tags: Grafana, Prometheus, Kubernetes, Datasource, YAML
- Summary: The `prometheusVersion` variable in Helm chart values does not set the Prometheus version in the datasource for Grafana in Kubernetes. 
- Friendly: Yes
- Concern: No
- Notes: It may be helpful to suggest checking the Prometheus version in use and ensure it is compatible with Grafana. Another suggestion could be to try manually setting the variable in the datasource configuration instead of in the YAML configuration. Additionally, asking for more details on the exact behavior after pod restart and any error messages received could aid in troubleshooting.
```
{
  "url": "https://community.grafana.com/t/want-to-download-dashboard-config-files/86209",
  "id": 86209,
  "slug": "want-to-download-dashboard-config-files",
  "title": "Want to download dashboard config files",
  "content": "<p>hi<br>\ni want to download all my grafana dashboard config files.i want to download all config files at once<br>\nwhere we have to navigate to download in GUI .<br>\nDo we have any specific path in CLI . or is there bash script for this .</p>\n<p>please help on this</p>"
}
```


## Recommendations: Want to download dashboard config files

- URL: https://community.grafana.com/t/want-to-download-dashboard-config-files/86209
- Tags: Dashboarding, GUI, CLI
- Summary: The poster wants to know how to download all their Grafana dashboard config files at once.
- Friendly: Yes
- Concern: No
- Notes: A friendly community member can suggest the poster to go to the Grafana web UI and navigate to each one of their dashboards, then click on the gear icon at the top-right corner and select the "JSON Model" option from the dropdown menu. The JSON files can then be downloaded and saved locally. Alternatively, they can use the Grafana API or CLI to download the dashboard files programmatically. A link to the Grafana API documentation can be provided for further information.
