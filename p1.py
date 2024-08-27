#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SONGS 100

// Structure to represent a song
typedef struct {
    char title[100];
    char artist[100];
} Song;

// Structure to represent a playlist
typedef struct {
    Song songs[MAX_SONGS];
    int count;
    int current_song;
} Playlist;

// Function to initialize a playlist
Playlist* createPlaylist() {
    Playlist* playlist = (Playlist*)malloc(sizeof(Playlist));
    if (playlist == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    playlist->count = 0;
    playlist->current_song = 0;
    return playlist;
}

// Function to add a song to the playlist
void addSong(Playlist* playlist, char* title, char* artist) {
    if (playlist->count < MAX_SONGS) {
        strcpy(playlist->songs[playlist->count].title, title);
        strcpy(playlist->songs[playlist->count].artist, artist);
        playlist->count++;
        printf("Song added to playlist!\n");
    } else {
        printf("Playlist is full!\n");
    }
}

// Function to remove a song from the playlist
void removeSong(Playlist* playlist, int index) {
    if (index >= 0 && index < playlist->count) {
        // Shift elements to the left to fill the gap
        for (int i = index; i < playlist->count - 1; i++) {
            playlist->songs[i] = playlist->songs[i + 1];
        }
        playlist->count--;
        printf("Song removed from playlist!\n");
    } else {
        printf("Invalid song index!\n");
    }
}

// Function to play the next song in the playlist
void playNextSong(Playlist* playlist) {
    playlist->current_song = (playlist->current_song + 1) % playlist->count;
    printf("Now playing: %s by %s\n", playlist->songs[playlist->current_song].title, playlist->songs[playlist->current_song].artist);
}

// Function to play the previous song in the playlist
void playPreviousSong(Playlist* playlist) {
    playlist->current_song = (playlist->current_song - 1 + playlist->count) % playlist->count;
    printf("Now playing: %s by %s\n", playlist->songs[playlist->current_song].title, playlist->songs[playlist->current_song].artist);
}

// Function to display the current song
void displayCurrentSong(Playlist* playlist) {
    printf("Current song: %s by %s\n", playlist->songs[playlist->current_song].title, playlist->songs[playlist->current_song].artist);
}

// Function to display the entire playlist
void displayPlaylist(Playlist* playlist) {
    if (playlist->count == 0) {
        printf("Playlist is empty!\n");
        return;
    }
    printf("Playlist:\n");
    for (int i = 0; i < playlist->count; i++) {
        printf("%d. %s by %s\n", i + 1, playlist->songs[i].title, playlist->songs[i].artist);
    }
}

int main() {
    Playlist* playlist = createPlaylist();

    int choice;
    char title[100], artist[100];
    int songIndex;

    do {
        printf("\nMedia Player Menu:\n");
        printf("1. Add song\n");
        printf("2. Remove song\n");
        printf("3. Play next song\n");
        printf("4. Play previous song\n");
        printf("5. Display current song\n");
        printf("6. Display playlist\n");
        printf("7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter song title: ");
                scanf("%s", title);
                printf("Enter artist: ");
                scanf("%s", artist);
                addSong(playlist, title, artist);
                break;
            case 2:
                printf("Enter song index to remove: ");
                scanf("%d", &songIndex);
                removeSong(playlist, songIndex - 1);
                break;
            case 3:
                playNextSong(playlist);
                break;
            case 4:
                playPreviousSong(playlist);
                break;
            case 5:
                displayCurrentSong(playlist);
                break;
            case 6:
                displayPlaylist(playlist);
                break;
            case 7:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while (choice != 7);

    free(playlist);
    return 0;
}
