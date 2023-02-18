<p>1. Clone this repo</p>
<p>2. Run:</p>
<code>docker compose up airflow-init </code>
<code>docker build . --tag extending_airflow:latest</code>
<code>docker compose up</code>
<p>3. Go to localhost:8080 in your browser</p>
<p>4. Trigger the is459t1 DAG</p>
<p>5. Check the logs for any errors, or check local directory for the translated JSON file</p>
