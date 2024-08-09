# Cloud Front

CDN, 225+ point globally, security protect

1. HTTP/HTTPS/Web socket support
2. integrated with WAF,Shield, Route53
3. Content cached, TTL
4. Support Cross Region replication

Origin resources:

1. S3 Bucket
2. Media store container
3. Customer origin, Http backends(ALB, EC2), the backend must be public and allow access from cloud front, we can use custom header(keep secret) to only allow cloud front access backends
4. Support orgin groups for fail over, can cross region

307 temporary Redirect scenario: when use s3 as origin, it may take 24 hours to propagate new bucket to all the regions. If we want to avoid it, we can add the region in source.

Geo Restriction:

1. header
2. allow list
3. block list

Pricing: different country vary, class all/200/100 to reduce cost

Cloud front signed URL for special security requirement.

Support Custom error response.

## Edge Function

1. Cloud front functions: deployed at cloud front location; js;no access to network/fs/request body
2. lambda@edge: deployed at regional edge cache; js & python

# Elastic Cache

Managed Redis or Memcache

Redis vs Memcache: Memcached is designed for simplicity while Redis offers a rich set of features that make it effective for a wide range of use cases.
