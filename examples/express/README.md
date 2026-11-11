# Express example (illustrative)

Review the API contract, then propose status-preserving error handling. Keep the audit read-only until the user approves a patch. This example is conceptual; it is not a drop-in middleware package.

```js
app.get('/orders/:id', async (req, res, next) => {
  try {
    const response = await fetch(orderUrl(req.params.id), {
      signal: AbortSignal.timeout(5_000),
    });
    if (!response.ok) {
      throw new UpstreamError(response.status, response.headers.get('retry-after'));
    }
    return res.json(await response.json());
  } catch (error) {
    return next(error);
  }
});
```

Questions: Is the operation safe to retry? Does the client contract already specify an error body? Is cancellation supported? Are logs redacted and correlated? Never expose `error.stack` in the response.
