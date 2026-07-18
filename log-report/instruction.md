Read the Apache-style access log at `/app/access.log` and summarize its traffic.

Success criteria:

1. Create `/app/report.json` containing a valid JSON object.
2. The object must contain exactly the keys `total_requests`, `unique_ips`, and
   `top_path`.
3. `total_requests` must be the number of non-empty log entries.
4. `unique_ips` must be the number of distinct client IP addresses.
5. `top_path` must be the most frequently requested path. If multiple paths are
   tied, use the one whose first request appears earliest in the log.
