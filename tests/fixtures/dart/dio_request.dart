Future<void> load(Dio dio) async {
  try {
    await dio.get('/profile');
  } on DioException catch (error) {
    print(error);
  }
}
