import { Discord, Github, Telegram, Twitch } from '@/components/icons/socials'

interface SocialLinks {
  name: string
  url: string
  icon: any
  showInHeader: boolean
}

export const SocialLinksData: SocialLinks[] = [
  {
    name: 'Discord',
    url: 'https://discord.gg/pYV4PBV5YW',
    icon: Discord,
    showInHeader: false,
  },
  {
    name: 'Twitch',
    url: 'https://www.twitch.tv/magicxcmd',
    icon: Twitch,
    showInHeader: false,
  },
  {
    name: 'Github',
    url: 'https://github.com/haxgun/beatwave',
    icon: Github,
    showInHeader: true,
  },
  {
    name: 'Telegram',
    url: 'https://t.me/magicxcmd',
    icon: Telegram,
    showInHeader: false,
  },
]
