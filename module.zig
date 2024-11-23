const std = @import("std");

pub export fn add(a: i32, b: i32) i32 {
    return a + b;
}

pub export fn greet() void {
    std.debug.print("Hello from Zig!\n", .{});
}
