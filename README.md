# TODO
- [ ] Clean location actions
    * [ ] Use location functions (`setloc`, `addloc`, `dilateloc`, `getlocTL`)
    * [ ] Define `const`
- [ ] Replace CUnit Ptr -> EPD
    * [ ] Use `BuildCheck` -> `BuildCheckEPD`
    * [ ] Use `BuildReset` -> `BuildResetEPD`
    * [ ] Check first if all build queues are empty, then skip every `BuildCheckEPD`
- [ ] Remove unnecessary global variables
- [ ] Screen X, Y are user-local data (desync)
    - [ ] Let MSQC send synced coordinates
    - [ ] Don't evoke MSQC when screen is not moving
    - [ ] (Optional) Replace MSQC mouse with Screen + Relative Mouse XY
