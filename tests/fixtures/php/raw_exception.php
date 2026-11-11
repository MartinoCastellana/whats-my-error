<?php
try {
    run_task();
} catch (\Throwable $exception) {
    return response()->json(['error' => $exception->getMessage()], 500);
}
