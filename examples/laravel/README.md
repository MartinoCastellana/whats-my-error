# Laravel example (illustrative)

Review the existing exception renderers and public contract. Validation errors often have intentional framework responses; preserve them unless a change is approved.

```php
try {
    $response = Http::timeout(5)->get($url);
    $response->throw();
    return response()->json($response->json());
} catch (\Illuminate\Http\Client\RequestException $exception) {
    // Normalize at a reviewed boundary. Do not return exception text.
    report($exception); // Configure redaction in the actual logging channel.
    return response()->json([
        'error' => ['code' => 'WME-UPSTREAM', 'message' => 'Service temporarily unavailable.'],
    ], 503);
}
```

The status and message above are examples only; preserve the target application's documented provider mapping.
