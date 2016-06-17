# ex32

#=======#
# LOOPS #
#=======#

numbers = [1,2,3,4,5]


puts "traditional / pythonic loop:"
for item in numbers
  puts item
end
puts

puts "rubyesque style:"
numbers.each do |item|
  puts item
end
puts

puts "alternatve rubyesque:"
numbers.each  {|i| puts i}

puts "range:"
(0..5).each {|i| puts i}
