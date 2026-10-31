"""Transparent illustrative public grader; not tamper resistant."""
import importlib
import sys
CASES=[
    ([],{}),
    ([{"tenant":"a","key":"x","version":1,"value":7}],{"a/x":7}),
    ([{"tenant":"a","key":"x","version":2,"value":8},{"tenant":"a","key":"x","version":1,"value":3}],{"a/x":8}),
    ([{"tenant":"a","key":"x","version":1,"value":1},{"tenant":"b","key":"x","version":1,"value":2}],{"a/x":1,"b/x":2}),
]
def main(name):
    fn=importlib.import_module(name).reconcile
    count=0
    for i,(events,expected) in enumerate(CASES,1):
        ok=fn(events)==expected
        count+=ok
        print(f"case {i}: {'PASS' if ok else 'FAIL'}")
    print(f"{count}/{len(CASES)} public cases passed")
    return 0 if count==len(CASES) else 1
if __name__=="__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else "reference"))
