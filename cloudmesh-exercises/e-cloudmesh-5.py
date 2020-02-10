# sp20-516-233 E.Cloudmesh.Common.5

# Develop a  program that demonstrates the  use  ofcloudmesh.common.StopWatch
from cloudmesh.common.StopWatch import StopWatch

if __name__ == "__main__":
    # compare how fast the different implementations are
    numbers = [100, 200, 300, 400, 500, 600, 700, 800, 900,
               1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
               2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900]

    print("start of test1")
    StopWatch.start("test1")
    total_squares = 0
    for n in numbers:
        total_squares = total_squares + (n * n)
    StopWatch.stop("test1")
    print(StopWatch.get("test1"))

    print("start of test2")
    StopWatch.start("test2")
    total_squares2 = 0
    for i in range(0, len(numbers)):
        total_squares2 += (n * n)
    StopWatch.stop("test2")
    print(StopWatch.get("test2"))

    print("Benchmark")
    StopWatch.benchmark()
