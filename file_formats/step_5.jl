import JSON

# Read json
a = JSON.parsefile("v4.json")

# Pretend we're doing something
push!(a["languages"], "julia")

# Write json
open("v5.json", "w") do file
    write(file, JSON.json(a))
end
