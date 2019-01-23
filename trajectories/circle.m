x0 = 0.0;
y0 = 0.0;
r = 22;

num_of_points = 200;
x = zeros(num_of_points, 1);
y = zeros(num_of_points, 1);


for i = 0:num_of_points
    theta = i * 0.01;
    x(i+1) = 22 * sin(theta * pi);
    y(i+1) = 22 * cos(theta * pi);
end

plot(x, y);
