// Need to decode password based on how many times a dial is left pointing at 0 after a turn.
// Dial starts at fifty, and input is series of rotations, i.e.:
//
// L68
// L30
// R48
// L5
// R60
// L55
// L1
// L99
// R14
// L82
//
// If rotated past 99 or below 0, number should wrap around. With sample input, dial points at 0 three times.
const std = @import("std");

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();
    var buffer: [1024]u8 = undefined;
    var stdin = std.fs.File.stdin();
    var reader = stdin.reader(&buffer);
    const stdin_stream = &reader.interface;

    const rotations = try stdin_stream.allocRemaining(allocator, std.io.Limit.unlimited);
    const password1 = try part1(rotations);
    const password2 = try part2(rotations);
    std.debug.print("password with landing on 0: {d}\n", .{password1});
    std.debug.print("password with crossing 0: {d}\n", .{password2});
}

fn part1(rotations: []const u8) !i32 {
    var dial: i32 = 50;
    var passCount: i32 = 0;

    var rotateIter = std.mem.splitScalar(u8, rotations, '\n');

    while (rotateIter.next()) |rotation| {
        if (rotation.len < 2 or rotation.len == 0) continue;
        const rotateDir: i8 = if (rotation[0] == 'R') 1 else -1;
        const rotateDistance = try std.fmt.parseInt(i32, rotation[1..], 10);
        dial += rotateDistance * rotateDir;
        dial = @mod(dial, 100);
        if (dial == 0) {
            passCount += 1;
        }
    }
    return passCount;
}

fn part2(rotations: []const u8) !i32 {
    var dial: i32 = 50;
    var passCount: i32 = 0;

    var rotateIter = std.mem.splitScalar(u8, rotations, '\n');

    while (rotateIter.next()) |rotation| {
        if (rotation.len < 2 or rotation.len == 0) continue;
        const rotateDir: i8 = if (rotation[0] == 'R') 1 else -1;
        const rotateDistance = try std.fmt.parseInt(i32, rotation[1..], 10);
        for (0..@intCast(rotateDistance)) |_| {
            dial += rotateDir;
            dial = @mod(dial, 100);
            if (dial == 0) {
                passCount += 1;
            }
        }
    }
    return passCount;
}

test "part1 sample input" {
    const want = 3;
    const got = try part1("L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82");
    try std.testing.expectEqual(want, got);
}
test "part2 sample input" {
    const want = 6;
    const got = try part2("L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82");
    try std.testing.expectEqual(want, got);
}
