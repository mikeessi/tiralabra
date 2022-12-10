import sys
import analysis_tool as at

def main(iterations, size, algorithm):
    """
    Kutsuu analyysityökalua halutuilla parametreillä

    Args:
        iterations: Testikierrosten lukumäärä
        size: Testisokkelon koko
        algorithm: Testattava algoritmi
    """
    at.test_algorithm(iterations, size, algorithm)

if __name__ == "__main__":
    iters = int(sys.argv[1])
    maze_size = int(sys.argv[2])
    algo = int(sys.argv[3])
    main(iters,maze_size,algo)
