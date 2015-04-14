require 'json'

# Read the file
a = File.open( "v1.json", "r" ) do |f|
  JSON.load( f )
end

# Pretend we're doing something to the file
a[:location] = "Mt. Hood, Oregon"
a["languages"] << "ruby"

# Write the output
File.open( "v2.json", "w" ) do |f|
  f.write( JSON.dump( a ) )
end
