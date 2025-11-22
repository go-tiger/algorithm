def solution(nums):
    unique_pokemons = len(set(nums))
    max_pokemons_to_pick = len(nums) // 2
    return min(unique_pokemons, max_pokemons_to_pick)