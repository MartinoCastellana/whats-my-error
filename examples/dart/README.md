# Dart / Dio review example

The current skill provides review guidance, not a Dart parser. Inspect Dio interceptors, `DioException`, cancellation, retry plugins, and widget error states in the target app. Verify whether a retry is safe before recommending it.

```dart
try {
  final response = await dio.get('/profile', cancelToken: cancelToken);
  // Confirm the API contract's payload semantics as well as transport status.
  return Profile.fromJson(response.data);
} on DioException catch (error) {
  // Map to a stable domain error at the boundary; do not display raw `error`.
  rethrow;
}
```
