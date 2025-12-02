// The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
// Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
// None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)
// Part 1: What do you get if you add up all of the invalid IDs?
// Part 2: There are actually more invalid IDs - anything that repeats *at least* twice. What is the sum of all the (now) invalid IDs?
const std = @import("std");

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();
    var buffer: [1024]u8 = undefined;
    var stdin = std.fs.File.stdin();
    var reader = stdin.reader(&buffer);
    const stdin_stream = &reader.interface;

    const idRanges = try stdin_stream.allocRemaining(allocator, std.io.Limit.unlimited);
    const invalidIds1 = try part1(idRanges);
    const invalidIds2 = try part2(idRanges);
    std.debug.print("Sum of invalid IDs: {d}\n", .{invalidIds1});
    std.debug.print("Sum of extra invalid IDs: {d}\n", .{invalidIds2});
}

fn part1(ranges: []const u8) !usize {
    var invalidSum: usize = 0;

    var rangeIter = std.mem.splitScalar(u8, ranges, ',');
    return while (rangeIter.next()) |range| {
        const rangeTrimmed = std.mem.trim(u8, range, "\n\r ");
        const rangeIndex = std.mem.indexOf(u8, rangeTrimmed, "-") orelse 0;
        const idEnds = [_][]const u8{ rangeTrimmed[0..rangeIndex], rangeTrimmed[(rangeIndex + 1)..] };

        const start = try std.fmt.parseInt(usize, idEnds[0], 10);
        const end = try std.fmt.parseInt(usize, idEnds[1], 10);
        for (start..end + 1) |id| {
            var buf: [15]u8 = undefined;
            const idStr = try std.fmt.bufPrint(buf[0..], "{d}", .{id});
            if (std.mem.eql(u8, idStr[0..(idStr.len / 2)], idStr[(idStr.len / 2)..])) invalidSum += id;
        }
    } else invalidSum;
}

fn part2(ranges: []const u8) !usize {
    var rangeIter = std.mem.splitScalar(u8, ranges, ',');
    var invalidSum: usize = 0;

    return while (rangeIter.next()) |range| {
        const rangeTrimmed = std.mem.trim(u8, range, "\n\r ");
        const rangeIndex = std.mem.indexOf(u8, rangeTrimmed, "-") orelse 0;
        const idEnds = [_][]const u8{ rangeTrimmed[0..rangeIndex], rangeTrimmed[(rangeIndex + 1)..] };

        const start = try std.fmt.parseInt(usize, idEnds[0], 10);
        const end = try std.fmt.parseInt(usize, idEnds[1], 10);
        for (start..end + 1) |id| {
            var buf: [30]u8 = undefined;
            const idStr = try std.fmt.bufPrint(buf[0..], "{d}", .{id});
            const search = try std.fmt.bufPrint(buf[0..], "{d}{d}", .{ id, id });
            if (std.mem.containsAtLeast(u8, search[1 .. search.len - 1], 1, idStr)) invalidSum += id;
        }
    } else invalidSum;
}

test "part1 sample input" {
    const want = 1227775554;
    const got = try part1("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124");
    try std.testing.expectEqual(want, got);
}
test "part2 sample input" {
    const want = 4174379265;
    const got = try part2("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124");
    try std.testing.expectEqual(want, got);
}
