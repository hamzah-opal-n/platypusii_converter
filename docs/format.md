# Platypus II Level Data Format

Like the first game, level data files in Platypus II are made up of a series of events that executed in order from the start of the file. Each event contains a wait time, action number and a set of arguments that are used to modify the action being executed. However, there are differences from the original Platypus.

## Event Structure

Unlike the original Platypus, each event is 40 bytes long and contains 10 values of type int32 (little-endian, 4 bytes long), regardless of the number of values actually used by the events.

```
Value No.     Name             Description
1             wait             time to wait before executing, in game ticks
2             action           action type to execute
3 - 10        arg1 - arg8      action-specific arguments
```

Unused values are typically set to 0. While all event values are stored as numbers internally, they are converted into text strings when decompiling to JSON format for ease of human readability.