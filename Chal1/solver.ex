defmodule Challenge do
  def loadfile(filename) do
    case File.read(filename) do
      {:ok, data} -> data
      {:error, _} -> IO.puts("Error reading from file: #{filename}")
    end
  end

  def solve_first() do
    "input"
    |> loadfile
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> Enum.chunk_every(2)
    |> Enum.map(&List.to_tuple/1)
    |> Enum.unzip()
    |> sortlists
    |> count_diff
    |> IO.inspect(label: "Total distance")
  end

  def solve_second() do
    "input"
    |> loadfile
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> Enum.chunk_every(2)
    |> Enum.map(&List.to_tuple/1)
    |> Enum.unzip()
    |> sortlists
    |> count_similarity
    |> IO.inspect(label: "Total similarity")
  end

  def sortlists({leftlist, rightlist}) do
    {Enum.sort(leftlist), Enum.sort(rightlist)}
  end

  def count_diff({leftlist, rightlist}) do
    Enum.zip_reduce(leftlist, rightlist, 0, fn a, b, acc ->
      abs(a - b) + acc
    end)
  end

  def count_similarity({leftlist, rightlist}) do
    leftlist
    |> Enum.dedup()
    |> Enum.reduce(0, fn a, acc ->
      a * Enum.count(rightlist, fn b -> b == a end) + acc
    end)
  end
end

Challenge.solve_first()
Challenge.solve_second()
