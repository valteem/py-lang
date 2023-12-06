def main():
    
    try:
        from functools import non_existent_import
    except:
        _non_existent_import = True
    
    print(_non_existent_import)

if __name__ == "__main__":
    main()