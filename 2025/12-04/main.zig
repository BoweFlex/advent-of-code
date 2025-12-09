// Input is a map of paper rolls. Rolls of paper are marked with an "@", and empty spots are marked with a ".".
// Part 1: Rolls of paper are only accessible if there are less than four rolls of paper in the eight adjacent positions. How many rolls of paper can be accessed by a forklift?
// Part 2: How many accessible rolls are there if you remove every accessible roll found?
const std = @import("std");

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();
    var buffer: [1024]u8 = undefined;
    var stdin = std.fs.File.stdin();
    var reader = stdin.reader(&buffer);
    const stdin_stream = &reader.interface;

    const input = try stdin_stream.allocRemaining(allocator, std.io.Limit.unlimited);
    const map = try splitMap(allocator, input);
    defer allocator.free(map);
    std.debug.print("Number of accessible rolls: {d}\n", .{try part1(map)});
    std.debug.print("Number of accessible rolls after removing any accessible rolls: {d}\n", .{try part2(map)});
}

fn part1(map: [][]u8) !usize {
    var accessibleRolls: usize = 0;
    return for (map, 0..map.len) |line, y| {
        for (line, 0..line.len) |spot, x| {
            if (line.len == 0 or spot != '@') continue;
            const filledAdjacent = [_]bool{
                (y > 0 and x > 0 and map[y - 1][x - 1] == '@'), // top left
                (y > 0 and map[y - 1][x] == '@'), // top middle
                (y > 0 and x < line.len - 1 and map[y - 1][x + 1] == '@'), // top right
                (x > 0 and map[y][x - 1] == '@'), // left
                (x < line.len - 1 and map[y][x + 1] == '@'), // right
                (y < map.len - 1 and x > 0 and map[y + 1][x - 1] == '@'), // bottom left
                (y < map.len - 1 and map[y + 1][x] == '@'), // bottom middle
                (y < map.len - 1 and x < line.len - 1 and map[y + 1][x + 1] == '@'), // bottom right
            };
            const isFilled = [_]bool{true};
            if (std.mem.count(bool, &filledAdjacent, &isFilled) < 4) accessibleRolls += 1;
        }
    } else accessibleRolls;
}

fn part2(map: [][]u8) !usize {
    var accessibleRolls: usize = 0;
    var rollRemoved: bool = true;
    return while (rollRemoved) {
        rollRemoved = false;
        for (map, 0..map.len) |line, y| {
            for (line, 0..line.len) |spot, x| {
                if (line.len == 0 or spot != '@') continue;
                const filledAdjacent = [_]bool{
                    (y > 0 and x > 0 and map[y - 1][x - 1] == '@'), // top left
                    (y > 0 and map[y - 1][x] == '@'), // top middle
                    (y > 0 and x < line.len - 1 and map[y - 1][x + 1] == '@'), // top right
                    (x > 0 and map[y][x - 1] == '@'), // left
                    (x < line.len - 1 and map[y][x + 1] == '@'), // right
                    (y < map.len - 1 and x > 0 and map[y + 1][x - 1] == '@'), // bottom left
                    (y < map.len - 1 and map[y + 1][x] == '@'), // bottom middle
                    (y < map.len - 1 and x < line.len - 1 and map[y + 1][x + 1] == '@'), // bottom right
                };
                const isFilled = [_]bool{true};
                if (std.mem.count(bool, &filledAdjacent, &isFilled) < 4) {
                    rollRemoved = true;
                    accessibleRolls += 1;
                    map[y][x] = '.';
                }
            }
        }
    } else accessibleRolls;
}

fn splitMap(allocator: std.mem.Allocator, map: []const u8) ![][]u8 {
    var mapIter = std.mem.splitScalar(u8, map, '\n');
    var newMap = std.ArrayList([]u8){};
    // defer newMap.deinit(allocator);
    return while (mapIter.next()) |line| {
        if (line.len == 0) continue;
        const mutable_line = try allocator.dupe(u8, line);
        try newMap.append(allocator, mutable_line);
    } else newMap.toOwnedSlice(allocator);
}

test "part1" {
    const allocator = std.testing.allocator;
    const map =
        \\..@@.@@@@.
        \\@@@.@.@.@@
        \\@@@@@.@.@@
        \\@.@@@@..@.
        \\@@.@@@@.@@
        \\.@@@@@@@.@
        \\.@.@.@.@@@
        \\@.@@@.@@@@
        \\.@@@@@@@@.
        \\@.@.@@@.@.
    ;
    const mapSplit = try splitMap(allocator, map);
    defer {
        for (mapSplit) |row| allocator.free(row);
        allocator.free(mapSplit);
    }
    const want = 13;
    const got = try part1(mapSplit);
    try std.testing.expectEqual(want, got);
}

test "part2" {
    const allocator = std.testing.allocator;
    const map =
        \\..@@.@@@@.
        \\@@@.@.@.@@
        \\@@@@@.@.@@
        \\@.@@@@..@.
        \\@@.@@@@.@@
        \\.@@@@@@@.@
        \\.@.@.@.@@@
        \\@.@@@.@@@@
        \\.@@@@@@@@.
        \\@.@.@@@.@.
    ;
    const mapSplit = try splitMap(allocator, map);
    defer {
        for (mapSplit) |row| allocator.free(row);
        allocator.free(mapSplit);
    }
    const want = 43;
    const got = try part2(mapSplit);
    try std.testing.expectEqual(want, got);
}
