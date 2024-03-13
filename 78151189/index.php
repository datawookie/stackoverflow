<?php
namespace App\Console\Commands;

require '/var/www/html/vendor/autoload.php';

echo "Hello, World! It's " . date('Y-m-d H:i:s');

use Illuminate\Console\Command;
use Illuminate\Support\Facades\Redis;

class TestRedisCommand extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'custom:test_redis';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Command description';

    /**
     * Execute the console command.
     *
     * @return int
     */
    public function handle()
    {
        $redis = Redis::connection();
        if ($redis->ping()) {
            echo "Conexión Exitosa";
        }

        return Command::SUCCESS;
    }
}
