// okay copilot, give me code from Wynncraft
// https://wynncraft.com/g/copilot/

public class WynncraftCopilot {
    public static void main(String[] args) {
              try {
            String url = "https://wynncraft.com/g/copilot/";
            Document doc = Jsoup.connect(url).get();

            String playerName = doc.select("div.player-name").text();
            String playerRank = doc.select("div.player-rank").text();
            String playerLevel = doc.select("div.player-level").text();
            String playerXp = doc.select("div.player-xp").text();
            String playerCoins = doc.select("div.player-coins").text();
            String playerLocation = doc.select("div.player-location").text();
            String playerWorld = doc.select("div.player-world").text();

            System.out.println("Player Name: " + playerName);
            System.out.println("Player Rank: " + playerRank);
            System.out.println("Player Level: " + playerLevel);
            System.out.println("Player XP: " + playerXp);
            System.out.println("Player Coins: " + playerCoins);
            System.out.println("Player Location: " + playerLocation);
            System.out.println("Player World: " + playerWorld);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void getPlayerStats(String playerName) {
        try {
            String url = "https://wynncraft.com/g/copilot/" + playerName;
            Document doc = Jsoup.connect(url).get();

            String playerRank = doc.select("div.player-rank").text();
            String playerLevel = doc.select("div.player-level").text();
            String playerXp = doc.select("div.player-xp").text();
            String playerCoins = doc.select("div.player-coins").text();
            String playerLocation = doc.select("div.player-location").text();
            String playerWorld = doc.select("div.player-world").text();

            System.out.println("Player Name: " + playerName);
            System.out.println("Player Rank: " + playerRank);
            System.out.println("Player Level: " + playerLevel);
            System.out.println("Player XP: " + playerXp);
            System.out.println("Player Coins: " + playerCoins);
            System.out.println("Player Location: " + playerLocation);
            System.out.println("Player World: " + playerWorld);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void getPlayerStats(String playerName, String playerRank, String playerLevel, String playerXp, String playerCoins, String playerLocation, String playerWorld) {
        try {
            String url = "https://wynncraft.com/g/copilot/" + playerName;
            Document doc = Jsoup.connect(url).get();

            String playerRank = doc.select("div.player-rank").text();
            String playerLevel = doc.select("div.player-level").text();
            String playerXp = doc.select("div.player-xp").text();
            String playerCoins = doc.select("div.player-coins").text();
            String playerLocation = doc.select("div.player-location").text();
            String playerWorld = doc.select("div.player-world").text();

            System.out.println("Player Name: " + playerName);
            System.out.println("Player Rank: " + playerRank);
            System.out.println("Player Level: " + playerLevel);
            System.out.println("Player XP: " + playerXp);
            System.out.println("Player Coins: " + playerCoins);
            System.out.println("Player Location: " + playerLocation);
            System.out.println("Player World: " +

                    playerWorld);
        } catch (Exception e) {
            e.printStackTrace();
        }
        
}

