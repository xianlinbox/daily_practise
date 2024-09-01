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

### Typical solution for Online video

1.  Amazon S3 for storage,
2.  AWS Elemental MediaConvert for file-based video processing,
3.  Amazon CloudFront for delivery.
4.  A family of video streaming protocols including Apple’s HTTP Live Streaming (HLS), Dynamic Adaptive Streaming over HTTP (DASH), Microsoft’s Smooth Streaming (MSS), and Adobe’s HTTP Dynamic Streaming (HDS) improves the user experience by delivering video as it is being watched, generally fetching content a few seconds ahead of when it will be needed.
5.  To use HLS, Elemental MediaConvert will split the video into short segments and will also create a manifest file. CloudFront need point to the manifest file.

## Edge Function

1. Cloud front functions: deployed at cloud front location; js;no access to network/fs/request body
2. lambda@edge: deployed at regional edge cache; js & python

# Elastic Cache

Managed Redis or Memcache

Redis vs Memcache: Memcached is designed for simplicity while Redis offers a rich set of features that make it effective for a wide range of use cases.

Redis can enable authentication.
