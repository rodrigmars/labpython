import sys

def main():
    print("hello world")


if __name__ == "__main__":

    rc = 1
    
    try:
    
        main()
        rc = 0
    
    except Exception as e:
    
        print(f'Error: {e}', file=sys.stderr)
    
    sys.exit(rc)
