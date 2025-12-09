// Input is a series of "banks", each bank is a line and each number in that line is a battery. The number is the amount of "joltage" remaining in the battery.
// See https://adventofcode.com/2025/day/3 for example input
//
// Need to turn on exactly two batteries in each bank and activate the largest possible joltage for the bank. The batteries cannot be reordered.
// Part 1: What is the total output joltage after activating maximum output for each bank?
// For the sample input:
// 98 + 89 + 78 + 92 = 357
// Part 2: Maximum output is actually 12 batteries per bank. What is the total output joltage now?
// For the sample input:
// 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619
const std = @import("std");

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();
    var buffer: [1024]u8 = undefined;
    var stdin = std.fs.File.stdin();
    var reader = stdin.reader(&buffer);
    const stdin_stream = &reader.interface;

    const banks = try stdin_stream.allocRemaining(allocator, std.io.Limit.unlimited);
    const output1 = try part1(banks);
    const output2 = try part2(banks);
    std.debug.print("Maximum Joltage Total Output: {d}\n", .{output1});
    std.debug.print("Maximum Joltage Total Output with 12 batteries: {d}\n", .{output2});
}

fn part1(banks: []const u8) !usize {
    var totalOutput: usize = 0;
    var bankIter = std.mem.splitScalar(u8, banks, '\n');
    var maxJoltage: usize = 0;
    return while (bankIter.next()) |bank| : ({
        totalOutput += maxJoltage;
        maxJoltage = 0;
    }) {
        for (0..bank.len) |i| {
            const batt1: usize = bank[i] - '0';
            for ((i + 1)..bank.len) |j| {
                const batt2: usize = bank[j] - '0';
                const joltage = batt1 * 10 + batt2;
                maxJoltage = if (joltage > maxJoltage) joltage else maxJoltage;
            }
        }
    } else totalOutput;
}

fn part2(banks: []const u8) !usize {
    var totalOutput: usize = 0;
    var maxJoltage: usize = 0;
    var start: usize = 0;
    var i: usize = 12;

    var bankIter = std.mem.splitScalar(u8, banks, '\n');
    return while (bankIter.next()) |bank| : ({
        totalOutput += maxJoltage;
        maxJoltage = 0;
        start = 0;
        i = 12;
    }) {
        if (bank.len < 12) continue;
        while (i > 0) : (i -= 1) {
            var max: u8 = '0';
            const end = bank.len - i;
            for (start..end + 1) |j| {
                if (bank[j] > max) {
                    max = bank[j];
                    start = j + 1;
                }
            }
            maxJoltage += (max - '0') * std.math.pow(usize, 10, i - 1);
        }
    } else totalOutput;
}

test "part1 sample input" {
    const want = 357;
    const got = try part1(
        \\987654321111111
        \\811111111111119
        \\234234234234278
        \\818181911112111
    );
    try std.testing.expectEqual(want, got);
}

test "part2 sample input" {
    const want = 3_121_910_778_619;
    const got = try part2(
        \\987654321111111
        \\811111111111119
        \\234234234234278
        \\818181911112111
    );
    try std.testing.expectEqual(want, got);
}
